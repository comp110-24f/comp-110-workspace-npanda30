"""CQ04 File 2"""

__author__: str = "730767309"


def get_coords(xs: str, ys: str) -> None:
    index1: int = 0
    index2: int = 0
    while index1 < len(xs):  # subscription notation through the options for coordx
        index2 = 0
        while index2 < len(ys):  # subscription notation through the options for coordy
            print("(" + xs[index1] + ", " + ys[index2] + ")")
            index2 = index2 + 1  # use every y value for the current x
        index1 = index1 + 1  # then, increase x by 1 and repeat
