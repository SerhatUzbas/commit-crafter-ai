def long_function_1():
    """A long function that does nothing significant."""
    for i in range(100):
        print(f"Iteration {i}: Doing something...")


def long_function_2():
    """Another long function that performs a simple task."""
    total = 0
    for i in range(1, 1001):
        total += i
    print(f"The sum of the first 1000 numbers is: {total}")


def long_function_3():
    """Yet another long function that creates a list of squares."""
    squares = [i**2 for i in range(1, 101)]
    print("List of squares from 1 to 100:", squares)


def long_function_4():
    """A long function that simulates a countdown."""
    for i in range(10, 0, -1):
        print(f"Countdown: {i}")
    print("Liftoff!")


def long_function_5():
    """A long function that generates Fibonacci numbers."""
    fib_sequence = [0, 1]
    for i in range(2, 20):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    print("Fibonacci sequence up to 20 terms:", fib_sequence)


def long_function_6():
    """A long function that reverses a string."""
    original_string = "Hello, world!"
    reversed_string = original_string[::-1]
    print("Reversed string:", reversed_string)


def long_function_7():
    """A long function that checks for prime numbers."""
    primes = []
    for num in range(2, 101):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    print("Prime numbers up to 100:", primes)


def long_function_8():
    """A long function that prints a multiplication table."""
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i * j:4}", end="")
        print()


def long_function_9():
    """A long function that simulates a simple game."""
    import random

    number_to_guess = random.randint(1, 100)
    guess = None
    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
    print("Congratulations! You've guessed the number.")


def long_function_10():
    """A long function that prints a pattern."""
    for i in range(1, 6):
        print("*" * i)
