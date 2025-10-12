"""
This module contains the Mastermind application.
"""
from __future__ import annotations

from dataclasses import dataclass

from mastermind.board import Board
from mastermind.peg import Guess, Feedback, KeyPeg
from mastermind.player import CodeBreaker, CodeMaker


@dataclass
class Mastermind:
    """This class represents a Mastermind game."""

    board: Board
    maker: CodeMaker
    breaker: CodeBreaker

    def guess(self) -> Guess:
        """Have the ``CodeBreaker`` generate a guess."""
        return self.breaker.generate_guess(self.board.state, self.board.columns)

    def answer(self, guess: Guess) -> Feedback:
        """Have the ``CodeMaker`` generate an answer."""
        return self.maker.generate_feedback(guess)

    def play(self) -> bool:
        """Play a single game of Mastermind, returning ``True`` if the game was won, ``False`` otherwise."""
        solved = [KeyPeg.RED] * self.board.columns

        answer = None
        while answer != solved:
            guess = self.guess()
            answer = self.answer(guess)
            try:
                self.board.add_turn(guess, answer)
            except ValueError:
                return False
            else:  # print board state if game hasn't ended
                print(self.board)
        return True
