from CQs.cq07.find_max import find_and_remove_max

"""I will confirm I can find the max number."""

__author__ = "730767309"


def test_find_and_remove_max_returns() -> None:
    """Test that f&r max returns the expected value."""
    a: list[int] = [12, 15, 900, 80, 2000000]
    max = find_and_remove_max(a)
    # Without defining max, the assertion had nothing to use to compare, kept failing.
    assert max == 2000000


def test_find_and_remove_max_mutates() -> None:
    """Test that f&r max properly mutates the input."""
    a: list[int] = [12, 15, 900, 80, 2000000]
    find_and_remove_max(a)
    assert a == [12, 15, 900, 80]


def test_find_and_remove_max_edge_case() -> None:
    """Test an unconvential input."""
    # I chose negative numbers as an "unconvential input."
    d: list[int] = [-20, 3, -19]
    max = find_and_remove_max(d)
    assert max == 3
    assert d == [-20, -19]
