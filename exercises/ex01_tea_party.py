""""We are hosting a tea party!"""

__author__ = "730767309"


def main_planner(guests: int) -> None:
    """This function is the entrypoint and print point of my program."""
    print("A cozy tea party for " + str(guests) + " people!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Total cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


"""I was struggling with what to put as the print argument, but when I saw how the equals signs connected the inputs to the functions I'd written, it makes sense now! Yay!"""


def tea_bags(people: int) -> int:
    """How many guests are attending"""
    return people * 2


def treats(people: int) -> int:
    """Treats wanted as per teas drank."""
    return int((tea_bags(people=people)) * 1.5)


"""It took me forever, but I learned to use 'people' in both the params & args."""
"""I'm still struggling with converting type from int to int since it's Xing by 1.5."""
"""Update: I figured it out! Use int with the desired function definition as the argument."""


""""It makes more sense to call tea_bags so if the # of people changes, it updates both treats & TBs."""


def cost(tea_count: int, treat_count: int) -> float:
    """The price to purchase the goodies."""
    return tea_count * 0.5 + treat_count * 0.75


"""Not a clue what I'm doing tbqh... why is it asking for a brand new name for the parameters?"""
"""Decided not to complicate it with more calls and stick with the instructions; works fine now."""

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
