def _locate_pivot(lst: list[float], idx_start: int, idx_end: int) -> int:
    """
    Moves pivot to the proper place in list and returns its index.
    :param lst: examined list
    :param idx_start: the first index of the examined list
    :param idx_end: the last index of the examined list
    :return: index of pivot
    """
    # pivot is always the last value in the list
    pivot_value: float = lst[idx_end]

    idx_place: int = idx_start
    for idx_now in range(idx_start, idx_end):
        if lst[idx_now] <= pivot_value:
            lst[idx_now], lst[idx_place] = lst[idx_place], lst[idx_now]
            idx_place += 1

    lst[idx_end], lst[idx_place] = lst[idx_place], lst[idx_end]
    return idx_place


def quick_sort(
        lst: list[float],
        idx_start: int = 0,
        idx_end: int | None = None) -> None:
    """
    Quick sort sorting algorithm.
    :param lst: list to sort
    :param idx_start: the first index of the examined list
    :param idx_end: the last index of the examined list
    :return:
    """
    if not lst:
        return

    if idx_end is None:
        # default end index is index of the last element
        idx_end = len(lst) - 1

    if idx_start >= idx_end:
        return

    idx_pivot: int = _locate_pivot(lst, idx_start, idx_end)

    quick_sort(lst, idx_start, idx_pivot - 1)
    quick_sort(lst, idx_pivot + 1, idx_end)
