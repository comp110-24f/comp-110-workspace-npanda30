from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        self.value = val
        self.next = next

    def __str__(self) -> str:
        """Represent a Node object as a string."""
        rest: str = "?"
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


# last function reports the last value in the linked list

two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def last(head: Node) -> int:
    """Return the last value of a linked list."""
    if head.next is None:
        return head.value  # Base case
    else:
        return last(head.next)  # Recursive case


def recursive_range(start: int, end: int) -> Node | None:
    """Build a linked list recursively from start to end (not inclusive)."""
    # Raise an Exception with string "invalid use of recursive range"
    # Edge case!
    if start < 0 or start > end:
        raise ValueError("""Invalid use of recursive range""")
    if start == end:
        return None
    else:
        # Recursive case
        # Intuition: Handle the first case based on the specific call
        first: int = start
        # build the rest of the list using the builder function recursive
        rest: Node | None = recursive_range(start + 1, end)
        return Node(first, rest)


a: Node | None = recursive_range(2, 8)
b: Node | None = recursive_range(110, 112)
print(a)
print(b)

# print(last(one))  # Expect 2

# print(last(courses))  # Expect 301

# print(to_str(one))  # Expect 1 -> 2 -> None
