#!/usr/bin/env python3

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a list, or
        None if the list is empty.

    Args:
        lst: A list of elements

    Returns:
        First element of the list or None if the list is empty
    """
    if lst:
        return lst[0]
    else:
        return None
