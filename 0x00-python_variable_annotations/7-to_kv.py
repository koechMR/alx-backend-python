#!/usr/bin/env python3
''' rep module
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' key and its value
    '''
    return (k, float(v**2))
