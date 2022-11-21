# IDEA: Make a grid the size of the proportions of the console.
# import numpy as np

import numpy as np
import os

def get_grid():
    size = os.get_terminal_size()
    w = size.columns
    h = size.lines
    return (w,h)

if __name__ == "__main__":
    print(get_grid())