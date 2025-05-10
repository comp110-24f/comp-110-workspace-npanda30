"""Practicing Nodes."""

from __future__ import annotations

__author__ = "730767309"


# In-class lesson:


class Node:
    """Creating the template for all Nodes."""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """Initalizing any instantiation of a Node object."""
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


# This last function reports the last value in the linked list

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


# Usage Examples:
# print(last(one))  # Expect 2

# print(last(courses))  # Expect 301

# print(to_str(one))  # Expect 1 -> 2 -> None


# EX08 Begins Here!!


def value_at(head: Node | None, index: int) -> int:
    """Returns the data of the Node stored at the index."""
    next: int = 0  # establish a variable to return
    if head is None:  # If LL is empty...
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:  # Base case
        return head.value
    else:  # Recursive case: build upon
        next = value_at(head.next, index - 1)  # -1 works closer to base case of idx = 0
    return next


def max(head: Node | None) -> int:
    """Returns the greatest value in a LL of Nodes."""
    if head is not None:  # Qualifying statement, can't compare None
        if head.next is None:  # Happens upon reaching the last item in the LL
            return head.value  # Still have to return something to compare!
        if head.value >= max(head.next):  # Got this backwards at first...
            return head.value  # Work towards base case and compare new with existing
        else:
            return max(head.next)
    else:
        raise ValueError("Cannot call max with None")


# Usage Example:
# print(max(Node(20, Node(30, Node(10, None)))))


def linkify(items: list[int]) -> Node | None:
    """Returns a LL of Nodes given a list of ints."""
    if len(items) == 0:  # Happens AFTER the final value is reached
        return None
    return Node(items[0], linkify(items[1:]))


# Usage Example:
# print(linkify([30, 50, 30]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Multiplies each Node value by the factor; returns LL."""
    if head is not None:  # qualifying statement
        return Node(head.value * factor, scale(head.next, factor))
        # Increase value, run scale again to add to the linked list
    else:
        return None


# Usage Example:
# print(scale(linkify([1, 2, 3]), 2))
