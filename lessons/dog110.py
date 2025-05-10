"""Welcome to Dog110!"""

__author__ = "730767309"


def dog110(score: list[dict[str, str]], thresh: int, idx: int) -> bool:
    if idx < len(score):
        if int((score[idx])["score"]) < thresh:  # Base case
            return False
        elif dog110(score, thresh, idx + 1) is not False:
            return True
    else:
        raise ValueError("Cannot find an index out of range.")


def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    if len(scores) <= idx:
        raise IndexError("idx too high")
    elif int(scores[idx]["scores"]) < thresh:
        return False
    else:
        if len(scores) == idx + 1:
            return True
        else:
            print(f"Good dog, {scores[idx]["name"]}")
            return all_good(scores, thresh, idx + 1)


pack: list[dict[str, str]] = [
    {"name": "Nelli", "score": "10"},
    {"name": "Ada", "score": "9"},
    {"name": "Pip", "score": "7"},
]

# Example Usage:
print(all_good(scores=pack, thresh=10, idx=0))
# should return False
# print(dog110(scores=pack, thresh=7, idx=0))
# should return True
