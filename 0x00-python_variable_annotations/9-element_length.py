#!/usr/bin/env python3

""" Calculates the length of each element in  the input list """

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the input list.

    Args:
        lst (Iterable[Sequence]): The input iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains an element from lst and its length.
    """

    return [(i, len(i)) for i in lst]
