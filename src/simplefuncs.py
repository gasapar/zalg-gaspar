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

    f_n2: int = 0
    f_n1: int = 1
    f_n: int = -1
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


def allowed_knight_movements(idx1: int, idx2: int) -> tuple[list[int], list[int]]:
    """
    Returns lists of all possible movements of a knight from given coordinates.
    :param idx1: knight first coordinate
    :param idx2: knight second coordinate
    :return: two lists of allowed movements
    """
    idx1_diffs = [-1, -2, -2, -1, 1, 2, 2, 1]
    idx2_diffs = [2, 1, -1, -2, -2, -1, 1, 2]

    idx1_allowed = []
    idx2_allowed = []

    for idx in range(len(idx1_diffs)):
        # possible new coordinates of the knight
        idx1_new = idx1 + idx1_diffs[idx]
        idx2_new = idx2 + idx2_diffs[idx]

        if -1 < idx1_new < 8 and -1 < idx2_new < 8:
            # new coordinates are inside the board
            idx1_allowed.append(idx1_new)
            idx2_allowed.append(idx2_new)

    return idx1_allowed, idx2_allowed


def minimal_knight_movements(
        idx1_start: int,
        idx2_start: int,
        board: list[list[int]] | None = None,
        movement_number: int = 1,
) -> list[list[int]]:
    """
    Returns the minimal number of knight movements to all board tile from given coordinates.
    :param idx1_start:
    :param idx2_start:
    :param board:
    :param movement_number:
    :return: Board containing minimal movements needed to get knight to each tile.
    """
    if idx1_start < 0 or idx1_start > 7 or idx2_start < 0 or idx2_start > 7:
        # coordinates are not on the board
        raise ValueError

    if not board:
        # default board for initialization
        board = create_matrix(8, 8, float("inf"))
        board[idx1_start][idx2_start] = movement_number - 1

    idx1_allowed, idx2_allowed = allowed_knight_movements(
        idx1=idx1_start,
        idx2=idx2_start)

    for idx in range(len(idx1_allowed)):
        idx1_new = idx1_allowed[idx]
        idx2_new = idx2_allowed[idx]

        if board[idx1_new][idx2_new] > movement_number:
            # new minimal number of movements needed to reach this tile
            board[idx1_new][idx2_new] = movement_number
            # start additional movements from the new coordinates
            board = minimal_knight_movements(
                idx1_start=idx1_new,
                idx2_start=idx2_new,
                board=board,
                movement_number=movement_number + 1)

    return board


def single_move(disk_number: int, from_place: str, to_place: str) -> None:
    """
    Prints command to move a disk from one place to another.
    :param disk_number:
    :param from_place:
    :param to_place:
    :return: None
    """
    print("Move disk " + str(disk_number) + " from " + from_place + " to " + to_place + ".")


def hanoi_tower_moves(
        disk_count: int,
        from_place: str = "A",
        to_place: str = "C",
        help_place: str = "B",
        move_counter: int = 0) -> int:
    """
    Prints command to solve hanoi tower problem and returns the number of needed moves.
    :param disk_count:
    :param from_place:
    :param to_place:
    :param help_place:
    :param move_counter:
    :return:
    """
    if disk_count < 1:
        return move_counter

    move_counter = hanoi_tower_moves(
        disk_count - 1,
        from_place=from_place,
        to_place=help_place,
        help_place=to_place,
        move_counter=move_counter)

    single_move(disk_count, from_place=from_place, to_place=to_place)
    move_counter += 1

    move_counter = hanoi_tower_moves(
        disk_count=disk_count - 1,
        from_place=help_place,
        to_place=to_place,
        help_place=from_place,
        move_counter=move_counter)

    return move_counter
