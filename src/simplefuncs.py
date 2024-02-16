import math


def real_quadratic_roots(a: float, b: float, c: float) -> tuple[float, float]:
    """
    Calculates real roots of quadratic equation: a*x**2 + b*x + c
    :param a: nonzero quadratic term
    :param b: linear term
    :param c: constant term
    :return: roots of quadratic equation
    """
    # check if is quadratic
    if a == 0.0:
        raise ValueError
    # discriminant
    d = b ** 2.0 - 4.0 * a * c
    # single root case
    if d == 0.0:
        x1 = -0.5 * b / a
        return x1, x1
    # complex roots case
    if d < 0.0:
        return float('nan'), float('nan')
    # real root case
    sqrt_d = math.sqrt(d)
    x1 = 0.5 * (-b + sqrt_d) / a
    x2 = 0.5 * (-b - sqrt_d) / a
    return x1, x2


def print_tree(num_levels: int) -> None:
    """
    Prints tree into command line.
    :param num_levels: number of levels of the tree
    :return: None
    """
    if num_levels < 0:
        raise ValueError
    if num_levels == 0:
        return

    for index in range(num_levels):
        num_spaces = num_levels - index - 1
        num_stars = 2 * index + 1
        current_line = ' ' * num_spaces + '*' * num_stars
        print(current_line)


def fib_number_recursion(num: int) -> int:
    """
    Recursive implementation of fibonacci numbers.
    :param num: corresponds to n th fibonacci number
    :return: n th fibonacci number
    """
    if num < 0:
        raise ValueError
    if num < 2:
        return num

    return fib_number_recursion(num - 1) + fib_number_recursion(num - 2)


def fib_number_cyclus(num: int) -> int:
    """
    Cyclic implementation of fibonacci numbers.
    :param num: corresponds to n th fibonacci number
    :return: n th fibonacci number
    """
    if num < 0:
        raise ValueError

    if num < 2:
        return num

    f_n2 = 0
    f_n1 = 1
    for index in range(2, num + 1):
        f_n = f_n1 + f_n2
        f_n2 = f_n1
        f_n1 = f_n
    return f_n
