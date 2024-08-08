#!/usr/bin/python3
"""In a text file, there is a single character H.
Your text editor can execute only two operations in this file: Copy All
and Paste. Given a number n, write a method that calculates
the fewest number of operations needed to result in exactly n H
characters in the file.
Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""


def minOperations(n):
    """Calculates the fewest number of operations needed to result in exactly n H"""
    if n <= 1:
        return 0

    min_ops = float('inf')

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factor1 = i
            factor2 = n // i

            operations = factor1 - 1 + factor2 - 1
            min_ops = min(min_ops, operations)

            operations = factor2 - 1 + factor1 - 1
            min_ops = min(min_ops, operations)

    return min_ops if min_ops != float('inf') else 0
