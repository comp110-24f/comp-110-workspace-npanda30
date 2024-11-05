"""I am going to make a numbers guessing game."""

__author__ = "730767309"


def guess_a_number() -> None:
    x = int(input("Guess a number: "))
    secret: int = 7
    # It makes sense to define the local variable within its frame.
    print("Your guess was " + str(x) + ".")
    # Receiving an error from gradescope--change how I receive & return input
    if x == secret:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is " + str(secret) + ".")
    elif x > secret:
        print("Your guess was too high! The secret number is " + str(secret) + ".")
        # No idea why it won't let me use two elses :(


if __name__ == "__main__":
    guess_a_number()
