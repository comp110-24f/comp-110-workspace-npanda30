"""Basic syntax of lists."""

# Create an empty list
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

my_numbers.append(1.5)

# Creating an already-populated list
game_points: list[int] = [102, 86, 94]

game_points.append(94)

# Modifying by Index (possible because lists are mutable)
game_points[1] = 82

# Getting the Length
len(game_points)

# Removing an item
game_points.pop(2)

print(["hello", "hi", "hey"][2])


def display(int_list: list[int]) -> None:
    """Displays all elements of int_list"""
    index: int = 0
    while index < len(int_list):
        print(int_list[index])
        index += 1


display(game_points)

# String Analogy
# my_name: str = ""  # literal
# my_name: str = str()  # constructor
