#!/usr/bin/env python3
"""Module sum_list."""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of floats and returns their sum.

    args:
        input_list: List of floats

    return:
        Sum of the input list as a float
    """
    return float(sum(input_list))
