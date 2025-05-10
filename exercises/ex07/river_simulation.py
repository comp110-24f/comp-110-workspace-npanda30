"""An instance of the River class."""

__author__ = "730767309"


from exercises.ex07.river import River

my_river: River = River(num_fish=10, num_bears=2)

my_river.view_river()

my_river.one_river_day()  # am i supposed to be running one day or week
