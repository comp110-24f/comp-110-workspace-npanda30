"""List Utils - Replicating abstractions or something."""

__author__: str = "730767309"


def all(list1: list[int], number: int) -> bool:
    # determines if all ints in the list are the same as number
    index: int = 0
    acc_count: int = 0
    if len(list1) == 0:
        return False  # ensures program ends if list is empty
    while index < len(list1):
        if list1[index] == number:
            acc_count += 1
        index += 1
    if acc_count == len(
        list1
    ):  # returns true if # of #s in the list are the same as amt found
        return True
    else:
        return False


def max(list_size: list[int]) -> int:
    if len(list_size) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 0
    highest: int = list_size[index]  # can't start at 0, won't work for neg numbers
    while index < len(list_size):  # first number starts as "highest found"
        if list_size[index] > highest:
            highest = list_size[index]
        index += 1
    return highest


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    index: int = 0
    if len(first_list) != len(
        second_list
    ):  # can't be identical if they're not same length
        return False
    while index < len(first_list):
        if (
            first_list[index] != second_list[index]
        ):  # as soon as an unequal is found, give up
            return False
        else:
            index += 1
    return True


def extend(shortlist: list[int], addedlist: list[int]) -> None:
    index = 0
    while index < len(addedlist):
        shortlist.append(addedlist[index])  # tags the new list to the end of the old
        index += 1
