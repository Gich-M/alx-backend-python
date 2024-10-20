#!/usr/bin/env python3
"""Module safe_first_element."""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Retrieves first element of a sequence if it exists.

    Args:
        lst: A list of elements

    Returns:
        First element of the list or None if the list is empty
    """
    if lst:
        return lst[0]
    else:
        return None
