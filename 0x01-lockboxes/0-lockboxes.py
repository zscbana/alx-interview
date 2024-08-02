#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def canUnlockAll(boxes):
    """Solves the lock boxes puzzle """
    n = len(boxes)
    unlocked = set()
    queue = [0]
    unlocked.add(0)

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and key not in unlocked:
                unlocked.add(key)
                queue.append(key)

    return len(unlocked) == n
