def get_first(list1: list[str]) -> str:
    """Return first element."""
    return list1[0]


def remove_first(list1: list[str]) -> None:
    """Remove first element."""
    list1.pop(0)


def get_and_remove_first(list1: list[str]) -> str:
    """Remove and return first element."""
    first: str = list1[0]
    list1.pop(0)
    return first
