#!/usr/bin/python3
"""
0x07. Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise.
    """
    size = len(matrix)
    for layer in range(size // 2):
        edge = size - layer - 1
        for index in range(layer, edge):
            opposite = size - 1 - index
            temp = matrix[layer][index]
            matrix[layer][index] = matrix[opposite][layer]
            matrix[opposite][layer] = matrix[edge][opposite]
            matrix[edge][opposite] = matrix[index][edge]
            matrix[index][edge] = temp
