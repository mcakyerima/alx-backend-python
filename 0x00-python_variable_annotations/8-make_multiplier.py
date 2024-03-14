#!/usr/bin/env python3

"""Returns a function that multiplies a float by a given multiplier."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that multiplies a float by the multiplier.
    """


    def multiplier_function(x: float) -> float:
        """
        Multiply a float by the multiplier.

        Args:
            x (float): The float value to multiply.

        Returns:
            float: The result of multiplying x by the multiplier.
        """

        return x * multiplier

    return multiplier_function
