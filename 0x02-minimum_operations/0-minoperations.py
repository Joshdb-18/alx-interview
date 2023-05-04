#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to resukt in exactly n H characters
    in the file
    """
    if n <= 1:
        return 0

    # find the prime factors of n
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    # sum up the factors to get the minimum number of operations
    return sum(factors)
