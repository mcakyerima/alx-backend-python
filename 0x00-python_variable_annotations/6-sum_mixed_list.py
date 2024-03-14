#!/usr/bin/env python3

"""Calculates the sum of a list of integers and floats."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of int and floats to sum.

    Returns:
        float: The sum of the input list of integers and floats.
    """

    return float(sum(mxd_lst))
