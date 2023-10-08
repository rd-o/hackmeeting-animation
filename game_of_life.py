import numpy as np
import sys

#del sys.modules['png_to_array']
import png_to_array

ON = 255
OFF = 0


def init_grid(N):
    grid = png_to_array.file_to_array()
    return grid


def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0, 0, 255],
                       [255, 0, 255],
                       [0, 255, 255]])
    grid[i:i + 3, j:j + 3] = glider


def update(grid, n, m):
    new_grid = grid.copy()
    for i in range(n):
        for j in range(m):

            total = int((grid[i, (j - 1) % m] + grid[i, (j + 1) % m] +
                         grid[(i - 1) % n, j] + grid[(i + 1) % n, j] +
                         grid[(i - 1) % n, (j - 1) % m] + grid[(i - 1) % n, (j + 1) % m] +
                         grid[(i + 1) % n, (j - 1) % m] + grid[(i + 1) % n, (j + 1) % m]) / 255)

            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = OFF
            else:
                if total == 3:
                    new_grid[i, j] = ON

    grid[:] = new_grid[:]

    return grid
