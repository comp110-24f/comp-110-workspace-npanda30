def factorial(n: int) -> int:
    """Compute the factorial of n."""
    # Base Case
    if n == 0:
        return 1
    # Recursive case
    if n < 0:
        raise ValueError("You can't use negative numbers.")
    return n * factorial(n - 1)


print(factorial(n=1))
