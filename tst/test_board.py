import pytest

from mastermind.board import Board
from mastermind.peg import CodePeg, KeyPeg


def make_guess(cols):
    # simple deterministic guess helper
    colors = [CodePeg.RED, CodePeg.GREEN, CodePeg.YELLOW, CodePeg.BLUE, CodePeg.WHITE]
    return tuple(colors[i % len(colors)] for i in range(cols))


def make_feedback(cols):
    # arbitrary feedback sequence of correct length
    return tuple((KeyPeg.RED if i % 2 == 0 else KeyPeg.WHITE) for i in range(cols))


def test_add_turn_updates_state_and_returns_immutable_view():
    board = Board(rows=3, columns=4)
    guess = make_guess(board.columns)
    feedback = make_feedback(board.columns)

    state = board.add_turn(guess, feedback)

    # state is an immutable tuple of tuples
    assert isinstance(state, tuple)
    assert isinstance(state[0][0], tuple)
    assert isinstance(state[0][1], tuple)

    # board.state matches and length increments
    assert board.state == state
    assert len(board.state) == 1


def test_add_turn_wrong_guess_length_raises():
    board = Board(rows=3, columns=4)
    wrong_guess = make_guess(3)  # too short
    feedback = make_feedback(board.columns)

    with pytest.raises(ValueError):
        board.add_turn(wrong_guess, feedback)


def test_add_turn_raises_when_board_full():
    board = Board(rows=2, columns=3)

    g = make_guess(board.columns)
    f = make_feedback(board.columns)

    board.add_turn(g, f)
    board.add_turn(g, f)

    with pytest.raises(ValueError):
        board.add_turn(g, f)


def test_state_is_copy_and_not_mutable():
    board = Board(rows=2, columns=3)
    g = make_guess(board.columns)
    f = make_feedback(board.columns)

    board.add_turn(g, f)

    state_snapshot = board.state
    # internal mutation shouldn't be possible through state
    assert isinstance(state_snapshot, tuple)

    # add another turn and ensure previous snapshot didn't change
    board.add_turn(g, f)
    assert len(state_snapshot) == 1
    assert len(board.state) == 2


def test_board_str_has_rows_and_placeholders():
    board = Board(rows=3, columns=4)
    # one turn filled
    board.add_turn(make_guess(board.columns), make_feedback(board.columns))

    s = str(board)
    lines = s.splitlines()

    # should have exactly board.rows lines
    assert len(lines) == board.rows

    # non-empty first line should use CodePeg.__str__ (single letters)
    assert all(len(token.strip()) == 1 for token in lines[0].split("|"))

    # remaining lines should be placeholders 'x'
    for line in lines[1:]:
        assert line.replace(" ", "") == ("x|" * (board.columns - 1) + "x")
