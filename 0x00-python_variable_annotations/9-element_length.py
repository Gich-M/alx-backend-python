#!/usr/bin/env python3
"""Module element_length."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates lenth of a list of sequences.

    Args:
        lst: A sequence of sequences
    Return:
        A list of tuples with each tuple containing a sequence
        and its length
    """

    return [(i, len(i)) for i in lst]
