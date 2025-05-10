"""File to define Bear class."""

__author__ = "730767309"


class Bear:
    """Establishes a template for all Bears."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes any instance of the Bear class."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Updates a bear's age and hunger."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Updates a bear after a meal."""
        self.hunger_score += num_fish
