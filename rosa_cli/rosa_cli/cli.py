# -*- coding: utf-8 -*-

"""Console script for rosa_cli."""
import sys
import click

from . import longest_increasing_subsequence, longest_decreasing_subsequence


@click.group()
def main():
    """Console script for rosa_cli."""
    return 0


@main.command(
    "lgis", short_help="Longest-monotonic subsequences"
)
@click.argument(
    "filepath", metavar="<filepath>"
)
def lgis(filepath):
    """This command prints the longest increasing and the longest decreasing
    subsequence from a sequence of positive integers.
    """
    stream = open(filepath, "r").read().splitlines()
    perm = [int(x) for x in stream[1].split()]
    print(" ".join([str(x) for x in longest_increasing_subsequence(perm)]))
    print(" ".join([str(x) for x in longest_decreasing_subsequence(perm)]))


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
