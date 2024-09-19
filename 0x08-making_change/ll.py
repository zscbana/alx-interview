#!/usr/bin/python3
"""Contains the calculate_min_coins function."""


def calculate_min_coins(coin_denominations, target_amount):
    """Returns the fewest number of coins needed to meet the target amount."""
    if not coin_denominations:
        return -1
    if target_amount <= 0:
        return 0
    min_coins = 0
    sorted_coins = sorted(coin_denominations, reverse=True)
    for coin in sorted_coins:
        while coin <= target_amount:
            target_amount -= coin
            min_coins += 1
        if target_amount == 0:
            return min_coins
    return -1
