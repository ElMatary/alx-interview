#!/usr/bin/python3
"""
Module contains minOperations fun
"""


def minOperations(n):
    """AI is creating summary for minOperations

    Args:
        n (int): the factor to print H times

    Returns:
        int: least number of operations.
    """
    if not isinstance(n, int) or n <= 1:
        return 0

    ops = 0
    copy_value = 0
    items = 1
    left = n - items

    while left > 0:
        left = n - items
        if n % items == 0:
            ops = ops + 1
            copy_value = items

        items = items + copy_value
        ops = ops + 1
        left = n - items

    return ops
