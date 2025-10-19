"""
This module contains the Peg classes for Mastermind.
The ``CodePeg`` and ``KeyPeg`` classes represent pegs used for guessing and answering respectively.
"""

from enum import StrEnum
from random import choice
from typing import Sequence, TypeAlias


class CodePeg(StrEnum):
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"
    BLUE = "blue"
    WHITE = "white"
    """Code pegs are used to represent the code and guesses."""


    @classmethod
    def random(cls) -> "CodePeg":
        return choice(list(cls.__members__.values()))

    def __str__(self) -> str:
        return self.value[0].upper()


class KeyPeg(StrEnum):
    RED = "red"
    WHITE = "white"
    """Key pegs are used to represent feedback for a guess."""

    """Correct color and position."""

    """Correct color, wrong position."""


Guess: TypeAlias = Sequence[CodePeg]
"""A guess is a sequence of ``CodePeg`` objects."""

Feedback: TypeAlias = Sequence[KeyPeg]
"""Feedback is given as a sequence of ``KeyPeg`` objects."""
