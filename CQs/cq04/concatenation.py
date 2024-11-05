"""CQ04 File 1"""

__author__: str = "730767309"


def concat(str1: str, str2: str) -> str:
    return str1 + str2  # concatenates the inputs


if (
    __name__ == "__main__"
):  # restricts this example to only when i am using concatenationpy as primary file
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
