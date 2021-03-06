"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two inputs."""
    the_sum = num1 + num2
    return the_sum

# print add(2,3)


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    difference = num1 - num2
    return difference

# print subtract(8,6)


def multiply(num1, num2):
    """Multiply the two inputs together."""
    product = num1 * num2
    return product

# print multiply(8, 2)


def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    quotient = num1 / num2
    return quotient

# print divide(10, 2)


def square(num1):
    """Return the square of the input."""
    square = num1 ** 2
    return square

# print square(9)


def cube(num1):
    """Return the cube of the input."""
    cube = num1 ** 3
    return cube

# print cube(2)


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    power = num1 ** num2
    return power

# print power(2, 2)


def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    modulo = num1 % num2
    return modulo

# print mod(10, 5)


def multiplies_custom_sum(num1, num2, num3):
    """Returns the sum of the first two numbers muliplied by the third."""
    return (num1 + num2) * num3

# print multiplies_custom_sum(1, 2, 3)


def add_cubes(num1, num2):
    """Returns the sum of two cubes."""
    return (num1 ** 3) + (num2 ** 3)

# print add_cubes(3, 2)
