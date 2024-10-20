#!/usr/bin/env python3

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a new list where each element from the input
        list is repeated factor times.

    Args:
        lst: The input list
        factor: The number of times each element
            should be repeated (default: 2)

    Returns:
        A new list with each element repeated factor times
        in the same order as the input list
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
