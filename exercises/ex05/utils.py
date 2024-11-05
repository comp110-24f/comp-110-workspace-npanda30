"""We will test utils soon. But first, let's write them."""

__author__ = "730767309"


def only_evens(get_evens_nums: list[int]) -> list[int]:
    newnums: list[int] = []  # Create an empty list to build onto
    index: int = 0
    while index < len(get_evens_nums):
        if get_evens_nums[index] % 2 == 0:
            newnums.append(get_evens_nums[index])
        index += 1
    return newnums


def sub(sub_nums: list[int], start: int, end: int) -> list[int]:
    if start < 0:
        start = 0
    index: int = start
    subset: list[int] = []
    if sub_nums == [] or end <= 0 or start > len(sub_nums):
        return subset
    if end > len(sub_nums):
        end = len(sub_nums)  # minimize excessive endpoints
    while index < end:
        subset.append(sub_nums[index])  # build new subset list
        index += 1
    return subset


def add_at_index(canvas: list[int], add_num: int, index: int) -> None:
    canvas.append(0)
    if index >= len(canvas) or index < 0:
        raise IndexError("Index is out of bounds for the input list")
    rev: int = 1
    while rev < (len(canvas) - index):
        canvas[len(canvas) - rev] = canvas[len(canvas) - rev - 1]
        # shifting over, then working backwards
        # Otherwise, I was removing item x before correcting item x + 1
        rev += 1
    canvas[index] = (
        add_num  # finally get to add in the desired int in the created space
    )
