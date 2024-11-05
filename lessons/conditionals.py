def less_than_10(num: int) -> None:
    if num < 10:  # check if this is true
        print("Small")  # "then" block
    else:
        print("Big bumber!")
    print("This is the end of the function!")


def wake_up(alarm: bool) -> str:
    """Return a message based on if the alarm is going off."""
    if alarm is True:
        return "Wake up! Go to Comp 110!"
    else:
        return "Keep sleeping. You deserve it :)"


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "Match!"
    else:
        return "No match :("


print(check_first_letter(word="happy", letter="h"))
print(check_first_letter(word="happy", letter="s"))
