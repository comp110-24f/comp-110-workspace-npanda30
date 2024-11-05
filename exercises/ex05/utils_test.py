"""We will now test our utils."""

__author__ = "730767309"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


# Only evens tests
def test_only_evens_result():
    """Tests whether all evens remain."""
    test_list: list[int] = [3, 12, 21, 30]
    assert only_evens(test_list) == [12, 30]


def test_only_evens_unmutated():
    """Test to make sure input list was not mutated."""
    test_list: list[int] = [18, 11, 9, 4]
    only_evens(test_list)
    assert test_list == [18, 11, 9, 4]
    # Check that the identity of test_list hasn't changed.


def test_only_evens_edge():
    """Tests whether negative odds are removed."""
    test_list: list[int] = [-18, -11, -9, 4]
    assert only_evens(test_list) == [-18, 4]
    # edge case with unconvential input


# Subs tests
def test_sub_unmutated():
    """Test to ensure input list is not mutated."""
    test_list: list[int] = [5, 10, 25, 17, 19, 39]
    sub(test_list, 2, 5)
    assert test_list == [5, 10, 25, 17, 19, 39]
    # Check that the identity of test_list hasn't changed.


def test_sub_result():
    """Test whether outputs are the correct subset."""
    test_list: list[int] = [5, 10, 25, 17, 19, 39]
    assert sub(test_list, 2, 5) == [25, 17, 19]
    # Check that the function works as expected


def test_sub_edge():
    """Test what happens if given indexes are out of range."""
    test_list: list[int] = [5, 10, 25, 17, 19, 39]
    assert sub(test_list, -2, 9) == [5, 10, 25, 17, 19, 39]
    # Testing edge case to make sure improper inputs are accounted for


# At index tests
def test_add_at_index_mutates():
    """Test that input list is mutated."""
    test_list: list[int] = [4, 7, 8, 20]
    add_at_index(test_list, 3, 2)
    assert test_list != [4, 7, 8, 20]
    # Make sure that test_list is something new/has been changed


def test_add_at_index_reslut():
    """Test if the output is correct."""
    test_list: list[int] = [4, 7, 8, 20]
    add_at_index(test_list, 3, 2)
    assert test_list == [4, 7, 3, 8, 20]
    # Return type None, but testing if the resulting test_list has the right ints


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    with pytest.raises(IndexError):
        add_at_index([4, 7, 8, 20], 9, 5)
        # an IndexError is raised when index is 9, greater than the length of our list
