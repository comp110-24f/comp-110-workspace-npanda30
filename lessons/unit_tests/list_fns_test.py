from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first() -> None:
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert get_first(fruits) == "apples"


def test_remove_first() -> None:
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert remove_first(fruits) is None


# def test_get_and_remove_first() -> None:
# fruits: list[str] = ["apples", "oranges", "bananas"]
# assert get_and_remove_first(fruits) == "apples"

# test in terminal: python -m pytest lessons/unit_tests/list_fns_test.py


def test_remove_first_behavior() -> None:
    """Test that remove first removes the first element."""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    remove_first(fruits)
    assert fruits == ["oranges", "bananas"]


def test_first_edge_case() -> None:
    """Test that get_first works with empty list."""
    input: list[str] = []
    get_and_remove_first(input)
    assert input == []
