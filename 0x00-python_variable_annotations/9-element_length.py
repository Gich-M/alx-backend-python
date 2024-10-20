#!/usr/bin/env python3
"""Module element_length."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains
        a sequence and its length.

    Args:
        lst: A sequence of sequences
    Return:
        A list of tuples with each tuple containing a sequence
        and its length
    """

    return [(i, len(i)) for i in lst]
