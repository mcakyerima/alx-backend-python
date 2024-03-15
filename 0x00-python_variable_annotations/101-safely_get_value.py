#!/usr/bin/env python3

''' Safely gets a value from a dictionary based on given key. '''

from typing import Mapping, Any, TypeVar, Union

# Define a type variable for the return value
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: T = None) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary based on the given key.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to search for in the dictionary.
        default (Optional[T], optional): The default value to return
        if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key in the
        dictionary, or the default value if the key is not found.
    """

    if key in dct:
        return dct[key]
    else:
        return default
