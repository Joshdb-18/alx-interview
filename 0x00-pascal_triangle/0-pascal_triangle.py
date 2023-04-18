#!/usr/bin/python3
"""
Pascal triangle function
"""


def pascal_triangle(n):
    """Returns a list of integers representing
    the Pascal's triangle of n
    """

    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = pascal_triangle(n-1)
        row = [1]

        for i in range(1, n-1):
            row.append(triangle[-1][i-1] + triangle[-1][i])
        row.append(1)
        triangle.append(row)
        return triangle
