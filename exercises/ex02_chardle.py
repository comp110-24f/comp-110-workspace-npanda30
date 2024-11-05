"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730767309"
# Autograder tried to remove points for this even though I didn't change anything. Odd guy, but adding str might help


def input_word() -> str:
    """This function receives the word the user is trying to play."""
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        return word
        # I was using != and only had one return value, maybe autograder didn't like this
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        return word
        # really struggled with returning values including '' because the course guide made me think i had to; interestingly, this interfered with the program's ability to count the instances!


def input_letter() -> str:
    """This function receives the letter the user is checking for."""
    letter: str = input("Enter a single character: ")
    # do I need to repeat the word "str" anywhere? i'll find out.
    if len(letter) == 1:
        return letter
        # same problem and solution as above. whole function ended up being pretty similar to input_word
    else:
        print("Error: Character must be a single character.")
        exit()
        return letter


def contains_char(word: str, letter: str) -> None:
    """This function checks and reports back how many times the letter appears in the word of interest."""
    instances: int = 0
    print("Searching for " + letter + " in " + word)
    # interesting that I had to be sure to write this in above the rest of the code
    if word[0] == letter:
        print(letter + " found at index 0")
        instances = instances + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        instances = instances + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        instances = instances + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        instances = instances + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        instances = instances + 1
    if instances == 1:
        # curious if this will work or if i have to make it instances > 1
        # i'm back! i realized your grammar changes--instance vs instances. Interesting!
        print(str(instances) + " instance of " + letter + " found in " + word)
    elif instances > 1:
        print(str(instances) + " instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)


def main() -> None:
    """This is the entry point, tying all the above functions together."""
    contains_char(word=input_word(), letter=input_letter())
    # defining main was SO hard for NO reason.. it kept trying to double down on asking for input. eventually chose to change how i was calling the function within it.
    # i think i need a refresher or greater understanding of how calling main works and why it goes at the end.


if __name__ == "__main__":
    main()
