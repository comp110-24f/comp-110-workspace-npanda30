from __future__ import annotations
from tabulate import tabulate  # type: ignore (this just suppresses the warning.)


class DataFrame:
    """A new type of class. It is called DataFrames."""

    data: dict[str, list[str]]

    def __init__(self, data: dict[str, list[str]]):
        """Initalizes the DataFrame class."""
        return None

    def tabulate(self) -> None:
        print(tabulate(self.data, headers=list(self.data.keys()), tablefmt="grid"))
        """A method for the DataFrame class."""

    def head(self, rows: int) -> DataFrame:
        """Another method for the DataFrame class."""
        return DataFrame({})

    def __add__(self, other: DataFrame) -> DataFrame:
        """Yet another method for the DataFrame class."""
        return DataFrame({})

    def select(self, selected_columns: list[str]) -> DataFrame:
        """How are there so many methods for the DataFrame class."""
        return DataFrame({})

    def filter_by_col_value(self, column_name: str, col_value: str) -> DataFrame:
        """Filtering method for the greedy DataFrame class."""
        return DataFrame({})
