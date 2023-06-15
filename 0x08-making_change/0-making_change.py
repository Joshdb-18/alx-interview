#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    Determines he fewest number of coins needed to
    meet a given amount total.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        count += total // coin
        total %= coin

    return count if total == 0 else -1
