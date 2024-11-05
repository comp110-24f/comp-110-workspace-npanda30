from __future__ import annotations

"""I am practicing classes."""

__author__ = "730767309"


class Point:
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        self.x_init = x
        self.y_init = y

    def scale_by(self, factor: int):
        x = x * factor
        y = y * factor

    def scale(self, factor: int) -> Point:
        newpoint: Point = Point(x * factor, y * factor)
        return newpoint
