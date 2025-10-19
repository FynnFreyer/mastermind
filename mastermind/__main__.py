#!/usr/bin/env python3

"""
This is the entrypoint for the mastermind application.
"""

from __future__ import annotations

from argparse import ArgumentParser, Namespace
from pathlib import Path
from sys import stderr
from traceback import format_exception, format_exception_only

from mastermind.__about__ import __author__, __description__, __version__
from mastermind.app import Mastermind
from mastermind.board import Board
from mastermind.player import RandomHonestCodeMaker, SmartCodeBreaker

VERBOSE = False
SCRIPT_DIR = Path(__file__).parent.resolve()


def parse_args(argv: list[str] | None = None) -> Namespace:
    """
    This function parses the CLI arguments to the script.

    :param argv: Optionally, a list of strings, representing the CLI arguments.
    :returns: The parsed arguments in a ``Namespace`` object.
    """
    parser = ArgumentParser(
        description=__description__,
        epilog=f"written by {__author__}",
    )

    # TODO: add arguments

    # # Positionals
    # parser.add_argument("something", type=int,
    #                     help="some integer value")

    # Flags
    board_group = parser.add_argument_group("Board Settings", "These options control the board size and layout.")

    default_rows = 12
    default_cols = 4

    board_group.add_argument("-r", "--rows", type=int, default=default_rows,
                             help=f"how many rows the board should have (default: {default_rows})")
    board_group.add_argument("-c", "--columns", type=int, default=default_cols,
                             help=f"how many columns the board should have (default: {default_cols})")

    parser.add_argument("-v", "--verbose", action="store_true",
                        help="print more verbose output")
    parser.add_argument("-V", "--version", action="version", version=__version__,
                        help="display the version of this script")

    args = parser.parse_args(argv)

    global VERBOSE
    VERBOSE = args.verbose

    # TODO (optional): do further post processing/validation of args

    return args


def run_game(rows: int, cols: int) -> int:
    """
    Run a mastermind game on a board of size rows x cols.

    :param rows: Number of rows on the board.
    :param cols: Number of columns on the board.
    :returns: Zero if the game was won, non-zero otherwise.
    """
    board = Board(rows=rows, columns=cols)
    maker = RandomHonestCodeMaker(board)
    breaker = SmartCodeBreaker(rows, cols)
    game = Mastermind(board, maker, breaker)
    solved = game.play()
    return int(not solved)


def main(argv: list[str] | None = None) -> int:
    """
    The script entrypoint. This function is executed, when running the script.

    :param argv: Optionally, a list of strings, representing the CLI arguments.
    :returns: The exit code of the script. Non-zero indicates an error.
    """
    try:
        args = parse_args(argv)
        return run_game(args.rows, args.columns)
    except Exception as e:
        err_lines = format_exception(e) if VERBOSE else format_exception_only(e)
        err = "".join(err_lines)
        print(err, file=stderr)
        return 1


if __name__ == "__main__":
    exit(main())
