"""EX03 - Wordle - Welcome to the real Wordle."""

__author__: str = "730767309"

success = False


def input_guess(secret_word_len: int) -> str:
    """Collects a guess word from player and confirms its length."""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    # Important to place guess above the loop and use a non-text input field within the loop.
    while len(guess) != secret_word_len:
        # Continues prompting until they provide a guess of length of secretword
        print(f"That wasn't {secret_word_len} chars! Try again: ")
        guess = input()
    return guess
    # Even when I entered a 12-character word, I didn't receive the error message. why T_T
    # I figured it out! I had the first if statement set to if < when it should be if != secretlength
    # Important to set the whole function to return the initial word to be used in main function later


# Test
# print(input_guess(secret_word_len=len(secretword)))


def contains_char(searched_word: str, sought_char: str) -> bool:
    """This function will find instances of the sought character in desired word and tell you if any matches were found."""
    assert len(sought_char) == 1
    index: int = 0
    # Counts through each index of the user's guess.
    char_count: int = 0
    while index < len(searched_word):
        # I was using an if statement instead of a whlie loop for an hour. Oops!
        if searched_word[index] == sought_char[0]:
            char_count = char_count + 1
            index = index + 1
        else:
            index = (
                index + 1
            )  # When I increase the index outside of the nested loop, it fails to increase.
    if char_count == 0:
        # I learned that I was concluding/returning my function far too early... i messed with the indents so bool was returned at an indentation appropriate for the whole function.
        # Updates whether or not the desired letter is present.
        return False  # I keep getting False even when the char is present! Why?? Because my index was not updating due to where in/out of the loop it was placed.
    else:
        return True


# Test
# print(contains_char(searched_word="abc", sought_char="b"))


def emojified(guess: str, secretword: str) -> str:
    """Visually represents the accuracy of the player's guess."""
    assert len(guess) == len(secretword)
    # Needed to ensure the lengths were referring to correct keyword arguments--secretword, in particular.
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    output: str = ""
    while index < len(guess):
        # Function loops and checks for the right letter's presence until the end of the word.
        if guess[index] == secretword[index]:
            output = output + GREEN_BOX
        elif contains_char(searched_word=secretword, sought_char=guess[index]):
            output = output + YELLOW_BOX
        elif not (contains_char(searched_word=secretword, sought_char=guess[index])):
            # struggled with syntax to use the whole function as a bool--don't set equal to anything, just see if contains_char is T/F!
            output = output + WHITE_BOX
        index = index + 1
    return output


# print(emojified(guess="python", secret="python"))


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    success = False
    while turns < 7 and not (success):
        # keeps the game within 6 turns
        print(f"=== Turn {turns}/6 ===")
        guess = str(input_guess(len(secret)))
        # creates a value for guess by running the input function with the int argument.
        print(emojified(guess=guess, secretword=secret))
        # printing is crucial here to display your output for Real Wordle.
        if guess == secret:
            success = True
            # Actually allows you to win.
        else:
            turns = turns + 1
    if success:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")
        # No exit functions!


if __name__ == "__main__":
    main(secret="limbs")
