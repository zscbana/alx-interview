#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """validUTF8"""
    NumberBytes = 0

    Mask1 = 1 << 7
    Mask2 = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if NumberBytes == 0:

            while mask_byte & i:
                NumberBytes += 1
                mask_byte = mask_byte >> 1

            if NumberBytes == 0:
                continue

            if NumberBytes == 1 or NumberBytes > 4:
                return False

        else:
            if not (i & Mask1 and not (i & Mask2)):
                    return False

        NumberBytes -= 1

    if NumberBytes == 0:
        return True

    return False
