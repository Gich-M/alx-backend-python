#!/usr/bin/env python3
"""Module safety_get_value."""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Retrieves a value from a dict using a given key

    Args:
        dct: A dictionary
        key: The key to search for in the dictionary
        default: The default value to return
            if the key is not found

    Returns:
        The value associated with the given key in
            the dictionary, or the default value
            if the key is not found
    """
    if key in dct:
        return dct[key]
    else:
        return default
