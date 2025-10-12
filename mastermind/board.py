"""
This module contains the Board class, which represents a Mastermind board.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence, TypeAlias

from mastermind.peg import Feedback, Guess

Turn: TypeAlias = tuple[Guess, Feedback]
"""A turn is a tuple of a guess and feedback."""

BoardState: TypeAlias = Sequence[Turn]
"""A board state is represented as sequence of turns."""


@dataclass
class Board:
    """This class represents the visible part of a Mastermind board."""

    rows: int = 12
    """How many rows this board has."""

    columns: int = 4
    """How many columns this board has."""

    _state: list[Turn] = field(default_factory=list)
    """The state of the board in a (mutable) list."""

    def add_turn(self, guess: Guess, feedback: Feedback) -> BoardState:
        """Change the board state to the next turn. Returns the new state."""
        if len(guess) != self.columns:
            raise ValueError("Wrong number of pegs in guess")
        if len(self._state) >= self.rows:
            raise ValueError("Board is full")

        turn = (guess, feedback)
        self._state.append(turn)

        return self.state

    @property
    def state(self) -> BoardState:
        """The board state in an immutable form."""
        return tuple((tuple(guess), tuple(feedback)) for guess, feedback in self._state)

    def __str__(self) -> str:
        # TODO: visualize feedback too
        board = [[str(peg) for peg in guess] for guess, _feedback in self.state]
        while len(board) < self.rows:
            empty_col = ["x"] * self.columns
            board.append(empty_col)

        row_strings = []
        for row in board:
            row_strings.append(" | ".join(row))
        board_string = "\n".join(row_strings)
        return board_string + "\n"
