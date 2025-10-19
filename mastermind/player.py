"""
This module contains the Player classes, which represent the roles in a Mastermind game.
A ``CodeMaker`` is the player who makes the code, and a ``CodeBreaker`` is a player who tries to guess the code.

Players can use a strategy to generate guesses, the default strategies are randomness for code generation and guessing,
and honesty for generating the feedback.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from mastermind.board import Board, BoardState
from mastermind.peg import CodePeg, Feedback, Guess, KeyPeg


class CodeMaker(ABC):
    """The player who makes the code."""

    @abstractmethod
    def generate_code(self) -> Guess:
        """Generate a code for the board."""
        raise NotImplementedError

    @abstractmethod
    def generate_feedback(self, guess: Guess) -> Feedback:
        """Generate feedback for a guess."""
        raise NotImplementedError


@dataclass
class RandomHonestCodeMaker(CodeMaker):
    """A code maker that generates a random code and gives honest feedback."""

    board: Board
    """The board that the code is being made for."""

    code: Guess = field(init=False)
    """The code that the CodeMaker came up with."""

    def __post_init__(self):
        self.code = self.generate_code()

    def generate_code(self) -> Guess:
        return tuple(CodePeg.random() for _ in range(self.board.columns))

    def generate_feedback(self, guess: Guess) -> Feedback:
        feedback = []

        # lists to save pegs that don't match exactly
        non_exact_guess_pegs = []
        non_exact_solution_pegs = []

        # find exact matches and save rest into lists
        for guess_peg, solution_peg in zip(guess, self.code):
            exact_match = guess_peg == solution_peg
            if exact_match:
                feedback.append(KeyPeg.RED)
            else:
                non_exact_guess_pegs.append(guess_peg)
                non_exact_solution_pegs.append(solution_peg)

        # find inexact matches from lists of rest pegs
        for guess_peg in non_exact_guess_pegs:
            if guess_peg in non_exact_solution_pegs:
                non_exact_solution_pegs.remove(guess_peg)
                feedback.append(KeyPeg.WHITE)
        return feedback


@dataclass
class CodeBreaker(ABC):
    """The player who tries to guess the code."""

    rows: int
    """Number of rows on the board."""

    columns: int
    """Number of columns on the board."""

    @abstractmethod
    def generate_guess(self, board_state: BoardState) -> Guess:
        """Generate a guess for the given board state. Number of columns is given in case this is the first guess."""
        raise NotImplementedError


@dataclass
class RandomCodeBreaker(CodeBreaker):
    """A code breaker that generates random guesses."""
    memory: dict[tuple[CodePeg, ...], list[KeyPeg]] = field(default_factory=dict)

    def generate_guess(self, board_state: BoardState) -> Guess:
        random = [CodePeg.random() for _ in range(self.columns)]
        if not self.memory:
            return random
        # TODO: implement non-random strategy
        while random in self.memory:
            random = [CodePeg.random() for _ in range(self.columns)]
        return random
