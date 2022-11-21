# IDEA: Make a grid the size of the proportions of the console.
# import numpy as np

import numpy as np
import os

SIDE_CHARACTER = '#'

def get_grid(shape:tuple = None) -> np.array:
    """Returns an array of zeros that are either
    an inputted shape, or the shape of the terminal.

    Parameters
    ----------
    shape : tuple, optional
        A tuple consisting of a base and height, by default None

    Returns
    -------
    np.array
        A matrix of zeros with the dimensions of shape
    """
    if shape is None:
        shape = os.get_terminal_size()
    return np.zeros(shape)

def display_grid(grid:np.array):
    for row in grid:
        print(*row,'\n')
    
def translate_element(element:float):
    if element != 0: return SIDE_CHARACTER
    else: return 3*' ' + 'p' # printing is three times as tall as it is wide

def translate_grid(grid:np.array) -> np.array:
    vectorised_grid = np.vectorize(translate_element)
    return vectorised_grid(grid)

#################### ARCHIVE #########################

# def scale_axes(output:float,grid_shape:tuple) -> int:
#     x,y = grid_shape
#     dy = 1/y
#     points = [dy * i for i in range(y)]
#     for i in range(1,len(points)):
#         if points[i-1] < output <= points[i]:
#             return i
#     return None

######################################################

def plot_line(start:np.array,end:np.array,grid:np.array) -> np.array:
    shape = grid.shape
    x,y = shape

    dx = 1/x# one step on the x axis
    dy = 1/y # one step on the y axis

    # We essentially want to know the integer points on this curve. is there a way to scale the curve
    # eq of line: y = mx + c, y-y_1 = m(x-x_1) 
    x_0,y_0 = start
    x_1,y_1 = end

    if y_0 == y_1: # the case of a horizontal line
        grid[:][y_0] = 1 
        return grid
    if x_0 == x_1: # The case of a vertical line
        for i in range(y):
            grid[i][x_0] = 1
        return grid
    
    # scale start and end points to be within the unit box
    x_0,x_1 = x_0 * dx, x_1 * dx
    y_0,y_1 = y_0 * dy, y_1 * dy

    gradient = (y_0-y_1)/(x_0-x_1)
    line = lambda x : gradient * (x-x_1) + y_1
    for i in range(x):
        line_output = int(line(i))
        y_i = line_output
        if  y_i is None:
            continue
        else:
            grid[i][y_i] = 1
    return grid


if __name__ == "__main__":
    grid = get_grid((5,5))

    start = np.array([4,4])
    end = np.array([0,0])

    grid = plot_line(start,end,grid)

    # display_grid(translate_grid(grid))
    display_grid(grid)
