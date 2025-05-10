from __future__ import annotations


class Node:
    def __init__(self, value: list[int], next: Node | None):
        self.value = value  # A list of integers
        # Either another Node or None
        if next is None:
            self.next = None
        else:
            self.next = next


def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# print(factorial(6))


def sum_of_natural_numbers(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)


# print(sum_of_natural_numbers(3))


def sum_of_digits(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)


# print(sum_of_digits(1234))


def power(n: int, exp: int) -> int:
    if exp == 0:
        return 1
    else:
        return n * power(n, exp - 1)


# To do
def gcd(num1: int, num2: int) -> int:
    return 0


# To do
def reverse_string(words: list[str]) -> list[str]:
    new_string: list[str] = []
    return new_string


def fibonacci(n: int) -> int:
    x: int = 0
    if x == n:
        return 0
    else:
        return x + fibonacci(n)


# print(fibonacci(8))


def tingtang(n: int) -> int:
    if n <= 0:
        return -1
    elif n == 1:
        return 1
    elif n % 2 == 1:
        return n + tingtang(n - 1)
    else:
        return tingtang(n - 1)


print(tingtang(3))


def sum_node_values(node: Node | None) -> int:
    if node is None:
        return 0
    else:
        sum: int = 0
        for number in node.value:
            sum += number
    return sum + sum_node_values(node.next)


node3 = Node([7, 8, 9], None)
node2 = Node([4, 5], node3)
node1 = Node([1, 2, 3], node2)
# print("Sum of all values:", sum_node_values(node1))
