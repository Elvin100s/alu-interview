#!/usr/bin/python3
"""
Pascal's Triangle Module

Contains a function to generate Pascal's Triangle up to a given number of rows.
"""


def pascal_triangle(n):
    """Generates Pascal's Triangle up to n rows

    Args:
        n (int): Number of rows to generate

    Returns:
        list: List of lists representing Pascal's Triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
