import numpy as np
from rotations import *
from typing import List
import os


class rotating_sqaure:
    def __init__(self, side_length: int, rate: float, side_character: str):
        self.side = side_length
        self.shape = (int(np.ceil(np.sqrt(2) * side_length)),) * 2
        self.center = self.shape[0] // 2
        self.rate = rate
        self.grid = self.get_grid()
        self.side_character = side_character
        self.vertices = self.get_vertices()

    def get_vertices(self) -> List[np.array]:
        """Will generate a central square to begin with.

        Returns
        -------
        List[np.array]
            A list of 2D verecies
        """
        side = self.shape[0]
        first_quater = side // 4
        third_quater = (3 * side) // 4

        vertex1 = np.array([first_quater, first_quater])  # origin co-ordinate
        vertex2 = np.array([0, first_quater - 1])  # top left co-ordinate
        vertex3 = np.array([third_quater - 1, third_quater - 1])  # top right component
        vertex4 = np.array([third_quater - 1, 0])  # bottom right co-ordinate

        return [vertex1, vertex2, vertex3, vertex4]

    def get_grid(self) -> np.array:
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
        return np.zeros(self.shape)

    def display_grid(self):
        """Displays the grid to the terminal

        Parameters
        ----------
        grid : np.array
            A grid (matrix)
        """
        for row in self.translate_grid():
            print(*row, "\n")

    def translate_element(self, element: float):
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
            return self.side_character + 3 * " "
        else:
            return 4 * " "  # printing is four times as tall as it is wide

    def translate_grid(self) -> np.array:
        """Applies translate_element to every element using numpy.

        Parameters
        ----------
        grid : np.array

        Returns
        -------
        np.array
            A transformed grid
        """
        vectorised_grid = np.vectorize(self.translate_element)
        return vectorised_grid(self.grid)

    def plot_line(self, start: np.array, end: np.array) -> np.array:
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
        x, y = self.shape

        dx = 1 / x  # one step on the x axis
        dy = 1 / y  # one step on the y axis

        # We essentially want to know the integer points on this curve. is there a way to scale the curve
        # eq of line: y = mx + c, y-y_1 = m(x-x_1)
        x_0, y_0 = start
        x_1, y_1 = end
        try:
            if y_0 == y_1:  # the case of a horizontal line
                self.grid[:][y_0] = 1
                return True
            if x_0 == x_1:  # The case of a vertical line
                for i in range(y):
                    self.grid[i][x_0] = 1
                return True

            # scale start and end points to be within the unit box
            x_0, x_1 = x_0 * dx, x_1 * dx
            y_0, y_1 = y_0 * dy, y_1 * dy

            gradient = (y_1 - y_0) / (x_1 - x_0)
            line = lambda x: gradient * (x - x_0) + y_0
            for i in range(x):
                line_output = int(line(i))
                self.grid[i][line_output] = 1.0
            return True
        except:
            return False
        
    def draw_square(self):
        self.vertices

    def centralise_point(self, point: np.array) -> np.array:
        return point + np.array([self.center]*2)

    def centralise_points(self, *points) -> List[np.array]:
        return [self.centralise_point(point) for point in points]

    def rotate_square(
        self,
        angle: float,
    ) -> list:
        """Will rotate every vertex of a square by some angle
        about the center of the square.

        Parameters
        ----------
        angle : float
            in radians

        Returns
        -------
        list
            a list of the rotated vectors cast as integers
        """
        vector_matrix = np.stack(self.vertices, axis=1)
        rotated_matrix = rotate_point(vector_matrix, angle)
        transposed_rotated_matrix = rotated_matrix.transpose().astype(int)
        return self.centralise_points(*transposed_rotated_matrix)


if __name__ == "__main__":
    square = rotating_sqaure(3, 1, "#")

