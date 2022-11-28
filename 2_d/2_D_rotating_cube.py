# IDEA: Make a grid the size of the proportions of the console.
# import numpy as np

import numpy as np
import os

SIDE_CHARACTER = "#"


def get_grid(shape: tuple = None) -> np.array:
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


def display_grid(grid: np.array):
    """Displays the grid to the terminal

    Parameters
    ----------
    grid : np.array
        A grid (matrix)
    """
    for row in grid:
        print(*row, "\n")


def translate_element(element: float):
    """Translates a 1 to the character that defines the lines of
    the square.

    Parameters
    ----------
    element : float
        Element of the grid. (0 or 1)

    Returns
    -------
        Whatever the SIDE_CHARACTER is set to if the element equals 1, else 3 spaces.
    """
    if element != 0:
        return SIDE_CHARACTER + 3 * " "
    else:
        return 4 * " "  # printing is four times as tall as it is wide


def translate_grid(grid: np.array) -> np.array:
    """Applies translate_element to every element using numpy.

    Parameters
    ----------
    grid : np.array

    Returns
    -------
    np.array
        A transformed grid
    """
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


def plot_line(start: np.array, end: np.array, grid: np.array) -> np.array:
    """Will plot a line using an numpy array as a grid.

    Parameters
    ----------
    start : np.array
        Starting point
    end : np.array
        Ending point
    grid : np.array
        Grid to draw the line on

    Returns
    -------
    np.array
        The grid with a line plotted on it
    """
    shape = grid.shape
    x, y = shape

    dx = 1 / x  # one step on the x axis
    dy = 1 / y  # one step on the y axis

    # We essentially want to know the integer points on this curve. is there a way to scale the curve
    # eq of line: y = mx + c, y-y_1 = m(x-x_1)
    x_0, y_0 = start
    x_1, y_1 = end

    if y_0 == y_1:  # the case of a horizontal line
        grid[:][y_0] = 1
        return grid
    if x_0 == x_1:  # The case of a vertical line
        for i in range(y):
            grid[i][x_0] = 1
        return grid

    # scale start and end points to be within the unit box
    x_0, x_1 = x_0 * dx, x_1 * dx
    y_0, y_1 = y_0 * dy, y_1 * dy

    gradient = (y_1 - y_0) / (x_1 - x_0)
    line = lambda x: gradient * (x - x_0) + y_0
    for i in range(x):
        line_output = int(line(i))
        grid[i][line_output] = 1.0
    return grid


def rotation_matrix(angle: float) -> np.array:
    """Rotates a vector by a angle radians

    Parameters
    ----------
    angle : float
        Number of radians

    Returns
    -------
    np.array
        Rotation matrix for that angle.
    """
    cosine = np.cos(angle)
    sine = np.sin(angle)
    return np.array([[cosine, sine], [-sine, cosine]])


def rotate_point(point: np.array, angle: float) -> np.array:
    """Rotates a point by some angle

    Parameters
    ----------
    point : np.array
    angle : float

    Returns
    -------
    np.array
        rotated vector
    """
    return np.matmul(rotation_matrix(angle), point)


def rotate_square(angle: float, *vertices: np.array) -> list:
    """Will rotate every vertex of a square by some angle

    Parameters
    ----------
    angle : float
        in radians

    Returns
    -------
    list
        a list of the rotated vectors
    """
    vector_matrix = np.stack(list(vertices), axis=1)
    rotated_matrix = rotate_point(vector_matrix, angle)
    transposed_rotated_matrix = rotated_matrix.transpose().astype(int)
    return [*transposed_rotated_matrix]


def draw_square(*vertices: np.array, side_length: float) -> np.array:
    """Will return a grid with the specified square on

    Parameters
    ----------
    side_length : int
        Side length of the square

    Returns
    -------
    np.array
        A grid with a square drawn on it.
    """
    grid = get_grid((side_length, side_length))

    vertex1, vertex2, vertex3, vertex4 = vertices

    grid = plot_line(vertex1, vertex2, grid)
    grid = plot_line(vertex2, vertex3, grid)
    grid = plot_line(vertex3, vertex4, grid)
    grid = plot_line(vertex4, vertex1, grid)
    return grid


def rotate_grid(angle: float, side_length: float, *vertices: np.array) -> np.array:
    new_vertices = rotate_square(angle, *vertices)
    return draw_square(*new_vertices, side_length=side_length)


def widen_grid(grid: np.array, enlarge_by: int):
    """Will widen a grid so that we can view rotations.

    Parameters
    ----------
    grid : np.array
    enlarge_by : int
        An integer to add to the side length of the grid
    """
    horizontal_shape, vertical_shape = grid.shape

    enlarged_grid = get_grid(
        (horizontal_shape + enlarge_by, vertical_shape + enlarge_by)
    )
    for i in range(horizontal_shape):
        for j in range(vertical_shape):
            enlarged_grid[i + enlarge_by - 3][j + enlarge_by - 3] = grid[i][j]
    return enlarged_grid


if __name__ == "__main__":
    size = os.get_terminal_size()
    x = size.columns // 20

    vertex1 = np.array([0, 0])  # origin co-ordinate
    vertex2 = np.array([0, x - 1])  # top left co-ordinate
    vertex3 = np.array([x - 1, x - 1])  # top right component
    vertex4 = np.array([x - 1, 0])  # bottom right co-ordinate

    vector_list = [vertex1, vertex2, vertex3, vertex4]

    rotated_vertices = rotate_square(np.pi / 4, *vector_list)

    # grid = draw_square(*rotated_vertices,side_length=x)
    # enlarged_grid = widen_grid(grid,8)
    # display_grid(translate_grid(enlarged_grid))
    grid = get_grid((x, x))
    grid = plot_line(rotated_vertices[0], rotated_vertices[1], grid)
    display_grid(grid)