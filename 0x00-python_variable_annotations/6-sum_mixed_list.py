#!/usr/bin/env python3

""" annotation for the list """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """  return sum as a float in the function """
    return float(sum(mxd_lst))
