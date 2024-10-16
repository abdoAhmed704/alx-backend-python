#!/usr/bin/env python3
""" Complex types - functions"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function  multiplies a float by multiplier.
    """
    f: Callable[[float], float] = lambda x: x * multiplier
    return f
