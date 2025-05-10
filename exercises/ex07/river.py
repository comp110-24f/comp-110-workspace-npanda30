"""File to define River class."""

__author__ = "730767309"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Establishes a template and procedures for any river."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(
                Fish()
            )  # feels weird adding a new empty animal, but it's an instance
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Goes through each list and only keeps young animals."""
        new_fish: list[Fish] = []
        for idx in range(0, len(self.fish)):
            if self.fish[idx].age <= 3:  # Accidentally wrote the wrong count: 5
                new_fish.append(self.fish[idx])  # add to a new list of fish
        self.fish = new_fish  # update self.fish to only include young fish
        # Repeat for self.bears
        new_bears: list[Bear] = []
        for i in range(0, len(self.bears)):
            if self.bears[i].age <= 5:
                new_bears.append(self.bears[i])
        self.bears = new_bears
        return None

    def remove_fish(self, amount: int):
        """Ensures only the frontmost fish remain."""
        new_fish: list[Fish] = []
        for fish in range(amount, len(self.fish)):
            new_fish.append(
                self.fish[fish]
            )  # create a new list from the amount index onward
        self.fish = new_fish

    def bears_eating(self):
        """Updates fish depending on bears' appetite."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(num_fish=3)  # keyword argument
                self.remove_fish(3)  # interesting calling methods and self
        return None

    def check_hunger(self):
        """Removes any bears that are too hungry to survive."""
        new_bears: list[Bear] = []
        for idx in range(0, len(self.bears)):  # for each bear in self.bears
            if self.bears[idx].hunger_score >= 0:  # if that bear is too hungry...
                new_bears.append(self.bears[idx])  # they can be kept!
        self.bears = new_bears
        return None

    def repopulate_fish(self):
        """Adds fish once there are enough parents."""
        idx: int = 0
        n: int = len(self.fish)
        add_fish: int = (
            n // 2
        ) * 4  # CAN'T use len(self.fish) in loop, so i made a variable n
        while idx < add_fish:
            self.fish.append(Fish())
            idx += 1  # avoid infinite loop
        return None

    def repopulate_bears(self):
        """Adds bears once there are enough parents."""
        idx: int = 0
        n: int = len(self.bears)
        add_bears: int = n // 2  # same as above, can't rely on len(self.bears)
        while idx < add_bears:
            self.bears.append(Bear())  # add a new baby bear!
            idx += 1
        return None

    def view_river(self):
        """A dashboard to check animal stats."""
        print(f"~~~ Day {self.day}: ~~~")  # f strings keep the formatting consistent
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Scale up, loop to a week."""
        idx: int = 1
        while idx <= 7:  # must end on day 7
            self.one_river_day()
            idx += 1
