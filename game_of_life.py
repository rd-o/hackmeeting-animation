import numpy as np
import sys   
del sys.modules['png_to_array']
import png_to_array

ON = 255
OFF = 0

def init_grid(N):
    #grid = np.array([])
    #grid = np.zeros(N*N).reshape(N, N)
    #addGlider(1, 1, grid)
    grid = png_to_array.file_to_array()

    #return f"Hello, {name}!"
    return grid

def addGlider(i, j, grid):
 
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    0, 255],
                       [255,  0, 255],
                       [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider

def update(grid, N):
 
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
 
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)
 
            if grid[i, j]  == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
 
    grid[:] = newGrid[:]

    return grid
 
