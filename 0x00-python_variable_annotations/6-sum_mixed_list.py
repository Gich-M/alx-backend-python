#!/usr/bin/env python3
"""Module sum_mixed_list."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats, and returns their sum.

    args:
        mxd_lst: List of integers and floats

    return:
        Sum of the input list as a float
    """
    return float(sum(mxd_lst))
