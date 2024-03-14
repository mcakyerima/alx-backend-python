#!/usr/bin/env python3

"""Converts a string and an int/float to a tuple."""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a string and an int/float to a tuple.

    Args:
        k (str): The string value.
        v (Union[int, float]): The int or float value.

    Returns:
        Tuple[str, float]: A tuple containing the string k and the square of v as a float.
    """
    return (k, float(v**2))

