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


def minOperations(b):
    """Calculates the fewest number of operations needed to result
    in exactly n H characters in the """
    n = len(b)
    seen_boxes = set([0])
    unseen_boxes = set(b[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(b[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
