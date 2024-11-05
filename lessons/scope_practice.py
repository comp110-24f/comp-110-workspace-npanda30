"""Practicing scope!"""


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed."""
    copy: str = ""  # set up empty string to copy values over into
    index: int = 0
    while index < len(msg):
        # if the letter is NOT char
        if not (msg[index] == char):  # if msg[index] != char
            # add it to copy
            copy = copy + msg[index]  # copy = copy + msg[index]
        index += 1
    return copy


# create a variable called word with the value "yoyo"
word = "yoyo"  # GLOBAL variable
# print the result of calling your function with arguments word and "y"
print(remove_chars(msg=word, char="y"))
