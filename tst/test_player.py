import pytest

from mastermind.board import Board
from mastermind.player import RandomCodeBreaker, RandomHonestCodeMaker
from mastermind.peg import CodePeg


def test_random_honest_codemaker_generate_code_returns_correct_length_and_types():
    # Bypass __init__/__post_init__ due to init=False field on `code`
    cm = RandomHonestCodeMaker.__new__(RandomHonestCodeMaker)
    cm.board = Board(rows=12, columns=4)

    code = cm.generate_code()

    assert len(code) == cm.board.columns
    # ensure all are CodePeg
    assert all(isinstance(p, CodePeg) for p in code)


def test_random_codebreaker_generate_guess_returns_correct_length_and_types_when_memory_empty():
    breaker = RandomCodeBreaker()
    guess = breaker.generate_guess((), 4)

    assert isinstance(guess, list)
    assert len(guess) == 4
    assert all(isinstance(p, CodePeg) for p in guess)


def test_random_codebreaker_generate_guess_returns_correct_length_and_types_when_memory_present():
    breaker = RandomCodeBreaker()
    # Preload memory with an arbitrary entry
    some_code = (CodePeg.RED, CodePeg.GREEN, CodePeg.BLUE, CodePeg.WHITE)
    breaker.memory[some_code] = []

    guess = breaker.generate_guess((), 4)

    assert isinstance(guess, list)
    assert len(guess) == 4
    assert all(isinstance(p, CodePeg) for p in guess)
