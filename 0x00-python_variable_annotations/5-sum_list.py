#!/usr/bin/env python3

"""Calculates the sum of a list of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list (list[float]): The list of floats to sum.

    Returns:
        float: The sum of the input list of floats.
    """
    return float(sum(input_list))
