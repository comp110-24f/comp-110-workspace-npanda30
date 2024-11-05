"""We are writing utils for dictionaries."""

__author__ = "730767309"


def invert(forward: dict[str, str]) -> dict[str, str]:
    inverted: dict[str, str] = {}
    for key in forward:  # Goes through each key in the list
        if forward[key] in inverted:
            raise KeyError("You can't do that.")
        inverted[forward[key]] = key  # adds to new dict, but swapped
    return inverted


def favorite_color(colors: dict[str, str]) -> str:
    counters_dict: dict[str, int] = {}
    for names in colors:
        if colors[names] not in counters_dict:
            counters_dict[colors[names]] = 1  # sets up counters for each color
        if colors[names] in counters_dict:
            counters_dict[colors[names]] += 1  # adds to each color's counter
    favoritest: str = ""
    highest: int = 0  # set a baseline for counter
    for each in counters_dict:
        if counters_dict[each] > highest:
            highest = counters_dict[each]  # Make sure to compare ints, not strs
            favoritest = each  # Make sure to compare strs
    return favoritest


def count(input: list[str]) -> dict[str, int]:
    counters_dict: dict[str, int] = {}
    for color in input:
        if color not in counters_dict:
            counters_dict[color] = 1
        else:
            counters_dict[color] += 1
    return counters_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    alphabetized: dict[str, list[str]] = {}
    for word in words:
        if word[0].lower() not in alphabetized:
            alphabetized[word[0].lower()] = list()
            # Start at index 0! Or else you are cooked
            alphabetized[word[0].lower()].append(word)
            # Don't just start the list, add to it
        else:
            alphabetized[word[0].lower()].append(word)
    return alphabetized


def update_attendance(input: dict[str, list[str]], weekday: str, attendee: str) -> None:
    if weekday not in input:
        input[weekday] = [attendee]  # Set up and add to a list
    else:
        if attendee not in input[weekday]:
            input[weekday].append(attendee)
            # Add to the existing value list
