#!/usr/bin/env python3

''' Safely gets a value from a dictionary based on given key. '''

from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None ) -> Res:
    '''Retrieve a value safely from a dictionary.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to search for.
        default (Union[T, None], optional): The default value if the
        key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key in the dict,
            or the default value if the key is not found.
    '''

    if key in dct:
        return dct[key]
    else:
        return default

