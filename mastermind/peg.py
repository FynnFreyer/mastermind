"""
This module contains the Peg classes for Mastermind.
The ``CodePeg`` and ``KeyPeg`` classes represent pegs used for guessing and answering respectively.
"""

from enum import IntEnum
from random import choice
from typing import Sequence, TypeAlias


class CodePeg(IntEnum):
    """Code pegs are used to represent the code and guesses."""

    RED = 0
    GREEN = 1
    YELLOW = 2
    BLUE = 3
    WHITE = 4

    @classmethod
    def random(cls) -> "CodePeg":
        return choice(list(cls.__members__.values()))

    def __str__(self) -> str:
        return self.name[0]


class KeyPeg(IntEnum):
    """Key pegs are used to represent feedback for a guess."""

    RED = 0
    """Correct color and position."""

    WHITE = 1
    """Correct color, wrong position."""


Guess: TypeAlias = Sequence[CodePeg]
"""A guess is a sequence of ``CodePeg`` objects."""

Feedback: TypeAlias = Sequence[KeyPeg]
"""Feedback is given as a sequence of ``KeyPeg`` objects."""
