"""I am practicing while loops."""

__author__ = "730767309"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0  # didn't realize this had to be a separate variable from count!
    while index < len(phrase):  # almost started writing a condition
        if phrase[index] == search_char:  # does the order of these matter?
            count = count + 1
            index = index + 1
        else:  # forgot to put the colon here for SO long
            index = index + 1
    return count  # important to returning an int value
