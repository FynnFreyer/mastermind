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
        cp_solution = list(self.code)
        cp_guess = list(guess)
        for i in range(self.board.columns):
            idx = 1 - i
            if guess[idx] == cp_solution[idx]:
                cp_solution.pop(idx)
                cp_guess.pop(idx)
                feedback.append(KeyPeg.WHITE)
        for peg in cp_guess:
            if peg in cp_solution:
                cp_solution.remove(peg)
                feedback.append(KeyPeg.RED)
        return feedback


class CodeBreaker(ABC):
    """The player who tries to guess the code."""

    @abstractmethod
    def generate_guess(self, board_state: BoardState, columns: int) -> Guess:
        """Generate a guess for the given board state. Number of columns is given in case this is the first guess."""
        raise NotImplementedError


@dataclass
class RandomCodeBreaker(CodeBreaker):
    """A code breaker that generates random guesses."""
    memory: dict[tuple[CodePeg, ...], list[KeyPeg]] = field(default_factory=dict)

    def generate_guess(self, board_state: BoardState, columns: int) -> Guess:
        random = [CodePeg.random() for _ in range(columns)]
        if not self.memory:
            return random
        # TODO: implement non-random strategy
        return random
