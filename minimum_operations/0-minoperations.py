#!/usr/bin/python3
"""
Module for minOperations method.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters.
    Returns 0 if n is impossible to achieve.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations