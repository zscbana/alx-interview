#!/usr/bin/python3
""" Contains makeChange function"""


def makeChange(coins, sum):
    """
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if not coins or coins is None:
        return -1
    if sum <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= sum:
            sum -= coin
            change += 1
        if (sum == 0):
            return change
    return -1
