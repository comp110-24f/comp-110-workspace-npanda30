"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730767309"


def main() -> None:
    def input_word() -> str:
        word: str = input("Enter a 5-character word: ")
        if len(word) != 5:
            print("Error: Word must contain 5 characters.")
        return word

    def input_letter() -> str:
        letter: str = input("Enter a single character: ")
        if len(letter) != 1:
            print("Error: Character must be a single character.")
        return letter

    word = input_word()
    letter = input_letter()

    def contains_char(word: str = word, letter: str = letter) -> None:
        instances: int = 0
        print("Searching for " + letter + " in " + word)
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
        if instances != 0:
            print(str(instances) + " instances of " + letter + " found in " + word)
        else:
            print("No instances of " + letter + " found in " + word)

    contains_char(word=word, letter=letter)


if __name__ == "__main__":
    main()
