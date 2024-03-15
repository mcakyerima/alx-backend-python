#!/usr/bin/env python3

""" Safely returns the first element of a sequence or None if empty"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Safely returns the first element of a sequence or None if the sequence is empty.

    Args:
        lst (Sequence): The input sequence.

    Returns:
        Union[Any, None]: The first element of the sequence or None
    """

    if lst:
        return lst[0]
    else:
        return None
