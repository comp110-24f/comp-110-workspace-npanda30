"""Summing the elements of a list using different loops"""

__author__ = "730767309"


def w_sum(vals: list[float]) -> float:
    index: int = 0
    the_sum: float = 0
    while index < len(vals):
        the_sum = the_sum + vals[index]
        index += 1
    return the_sum


# Tests
# print(w_sum([1.1, 0.9, 1.0]))
# print(w_sum([]))


def f_sum(vals: list[float]) -> float:
    the_sum: float = 0
    for num in vals:
        the_sum = num + the_sum
    return the_sum


# Tests
# print(f_sum([1.1, 0.9, 1.0]))
# print(f_sum([]))


def f_range_sum(vals: list[float]) -> float:
    the_sum = 0
    for index in range(0, len(vals)):
        the_sum = vals[index] + the_sum
    return the_sum


# Tests
# print(f_range_sum([1.1, 0.9, 1.0]))
# print(f_range_sum([]))
