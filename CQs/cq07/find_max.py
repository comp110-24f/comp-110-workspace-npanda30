"""I will find the max number."""

__author__ = "730767309"


def find_and_remove_max(nums: list[int]) -> int:
    index: int = 0
    if nums == []:
        max = -1
        return max
    max = nums[0]
    while index < len(nums):
        if nums[index] > max:
            max = nums[index]
        index += 1
    # print(max) -- this part worked fine.
    index = 0
    # important to reset the index when moving to the next stage: removing max.
    while index < len(nums):
        # print(index) -- used when figuring out why my while loop wasn't working.
        if nums[index] == max:
            nums.pop(index)
        else:
            # Took me a HOT minute to realize that len(nums) was changing!
            index += 1
    return max
