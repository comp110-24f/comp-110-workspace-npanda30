"""Mutating functions."""

__author__ = "730767309"

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(parameter1: list[int], parameter2: int) -> None:
    parameter1.append(parameter2)


def double(list1: list[int]) -> None:
    index: int = 0
    while index < len(list1):
        list1[index] = 2 * int(list1[index])
        index += 1


double(list1=list_2)

print(list_1)
print(list_2)
