#!/usr/bin/env python3

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int or float and returns a tuple

    args:
        k: String
        v: Integer or float to be squared

    return:
        Tuple: First element of the tuple is the string k.
                Second element is the square of the
                int/float v and should be annotated
                as a float.
    """
    return (k, v ** 2)
