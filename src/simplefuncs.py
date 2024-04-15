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


def coinChange(value: int, coins: list[int] | None = None) -> list[int]:
    """
    Return list of coins needed to make a change. Uses greedy algorithm.
    :param value: value to be returned
    :param coins: list of coins/banknotes
    :return: list of used coins/banknotes
    """
    if value < 0:
        raise ValueError

    if value == 0:
        return []

    if not coins:
        # default CZK denominations
        coins: list[int] = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1_000, 2_000, 5_000]
    else:
        coins.sort(reverse=True)

    results: list[int] = []

    for coin_value in coins:
        coin_count: int = value // coin_value
        if coin_count == 0:
            continue
        results += [coin_value] * coin_count
        value -= coin_value * coin_count

        if value == 0:
            break
    return results


def find_value_in_ordered_list(value: float,
                               all_values: list[float],
                               index_first: int = 0,
                               index_last: int | None = None
                               ) -> int:
    """
    Finds the index off a value in an ordered list.
    :param value: value to look for
    :param all_values: list of values
    :param index_first:
    :param index_last:
    :return: index of the value in all_values or -1 if nothing found
    """
    if not all_values:
        return -1

    if index_last is None:
        index_last = len(all_values) - 1

    if value < all_values[0]:
        return -1
    if value > all_values[-1]:
        return -1

    middle_index: int = (index_first + index_last) // 2

    if all_values[middle_index] == value:
        return middle_index

    if index_first == index_last:
        return -1

    if value > all_values[middle_index]:
        return find_value_in_ordered_list(value, all_values, middle_index + 1, index_last)
    else:
        return find_value_in_ordered_list(value, all_values, index_first, middle_index - 1)


def print_as_matrix(lst: list[list[float]]) -> None:
    """
    Print a list of lists as a matrix.
    :param lst: matrix passed as list of lists
    :return: None
    """
    for row in lst:
        print(row)


def create_matrix(num_rows: int, num_columns: int, default_value: float = 0.0):
    """
    Create a matrix (list of lists) with fixed value.
    :param num_rows:
    :param num_columns:
    :param default_value:
    :return: matrix
    """
    return [[default_value] * num_columns for _ in range(num_rows)]
