from CQs.cq04.concatenation import concat  # allows us to join coords in this file
from CQs.cq04.coordinates import (
    get_coords,
)  # allows us to use this function on our desired global variables

"""CQ04 File 2"""

__author__: str = "730767309"


x: str = "123"
y: str = "abc"

print(concat(x, y))
get_coords(x, y)
