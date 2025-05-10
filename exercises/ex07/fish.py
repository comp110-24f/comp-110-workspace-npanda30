"""File to define Fish class."""

__author__ = "730767309"


class Fish:
    """Establishes a template for all fish."""

    age: int

    def __init__(self):
        """Initializes fish's ages."""
        self.age = 0
        return None

    def one_day(self):
        """Updates fish's ages."""
        self.age += 1
        return None
