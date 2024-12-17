def hello_world():
    """Prints a hello world message."""
    print("Hello, world!")


def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b


def factorial(n):
    """Calculates the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


if __name__ == "__main__":
    hello_world()
    print(f"Sum of 5 and 3 is: {add_numbers(5, 3)}")
    print(f"Factorial of 5 is: {factorial(5)}")
