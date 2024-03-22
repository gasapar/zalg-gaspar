import math


def real_quadratic_roots(a: float, b: float, c: float) -> tuple[float, float]:
    """
    Calculates real roots of quadratic equation: a*x**2 + b*x + c
    @param a: nonzero quadratic term
    @param b: linear term
    @param c: constant term
    @return: roots of quadratic equation
    """
    # check if is quadratic
    if a == 0.0:
        raise ValueError
    # discriminant
    d: float = b ** 2.0 - 4.0 * a * c
    # single root case
    if d == 0.0:
        x1: float = -0.5 * b / a
        return x1, x1
    # complex roots case
    if d < 0.0:
        return float('nan'), float('nan')
    # real root case
    sqrt_d: float = math.sqrt(d)
    x1: float = 0.5 * (-b + sqrt_d) / a
    x2: float = 0.5 * (-b - sqrt_d) / a
    return x1, x2


def print_tree(num_levels: int) -> None:
    """
    Prints tree text art into command line.
    @param num_levels: number of levels of the tree
    @return: None
    """
    if num_levels < 0:
        raise ValueError
    if num_levels == 0:
        return

    for index in range(num_levels):
        num_spaces = num_levels - index - 1
        num_stars = 2 * index + 1
        current_line = (' ' * num_spaces) + '*' * num_stars
        print(current_line)


def fib_number_recursion(num: int) -> int:
    """
    Recursive implementation of fibonacci numbers.
    @param num: corresponds to nth fibonacci number
    @return: nth fibonacci number
    """
    if num < 0:
        raise ValueError
    if num < 2:
        return num

    return fib_number_recursion(num - 1) + fib_number_recursion(num - 2)


def fib_number_cyclus(num: int) -> int:
    """
    Cyclic implementation of fibonacci numbers.
    @param num: corresponds to nth fibonacci number
    @return: nth fibonacci number
    """
    if num < 0:
        raise ValueError

    if num < 2:
        return num

    f_n2 = 0
    f_n1 = 1
    for _ in range(2, num + 1):
        f_n = f_n1 + f_n2
        f_n2 = f_n1
        f_n1 = f_n
    return f_n


def fib_number_close(num: int) -> int:
    """
    Implementation of fibonacci numbers using closed form.
    @param num: corresponds to nth fibonacci number
    @return: nth fibonacci number
    """
    if num < 0:
        raise ValueError

    if num < 2:
        return num

    sqrt5 = math.sqrt(5)
    phi = 0.5 * (1.0 + sqrt5)
    psi = 0.5 * (1.0 - sqrt5)

    return int(round((phi ** num - psi ** num) / sqrt5))


def min_of_list(lst: list[float]) -> tuple[float, int]:
    """
    Find minimum value of list together with index of the minimum.
    @param lst: non-empty list of values
    @return: minimum of list, index of the minimum
    """
    if not lst:
        raise ValueError

    min_value = float('inf')
    min_idx = -1
    for idx, value in enumerate(lst):
        if min_value > value:
            min_value = value
            min_idx = idx

    return min_value, min_idx
