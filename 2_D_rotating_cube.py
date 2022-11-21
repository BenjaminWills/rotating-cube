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

def display_grid(grid):
    for row in grid:
        print(*row,'\n')
    
def translate_element(element:float):
    if element != 0: return SIDE_CHARACTER
    else: return ' '

def translate_grid(grid):
    vectorised_grid = np.vectorize(translate_element)
    return vectorised_grid(grid)
    
if __name__ == "__main__":
    grid = get_grid((5,5))
    display_grid(translate_grid(grid))