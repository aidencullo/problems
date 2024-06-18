from itertools import zip_longest

import random
from copy import deepcopy
from pprint import pprint
import numpy as np


def check_sudoku(grid):
    def check_row(row):
        return len(set(row)) == len(row)

    def check_rows(grid):
        return all(check_row(row) for row in grid)

    def check_cols(grid):
        return check_rows(np.transpose(grid))

    def check_squares(grid):
        def to_squares(grid):
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    yield grid[i: i + 3, j: j + 3].flatten()

        return all(check_row(square) for square in to_squares(grid))

    grid = np.array(grid)
    return (check_rows(grid)
            and check_cols(grid)
            and check_squares(grid))














correct = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

assert check_sudoku(correct)







incorrect_row = deepcopy(correct)
incorrect_row[0][0], incorrect_row[1][0] = incorrect_row[1][0], incorrect_row[0][0]

assert not check_sudoku(incorrect_row)









incorrect_col = deepcopy(correct)
incorrect_col[0][0], incorrect_col[0][1] = incorrect_col[0][1], incorrect_col[0][0]

assert not check_sudoku(incorrect_col)









incorrect_square = deepcopy(correct)
incorrect_square[2], incorrect_square[3] = incorrect_square[3], incorrect_square[2]

assert not check_sudoku(incorrect_square)
