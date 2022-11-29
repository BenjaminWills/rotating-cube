import matplotlib.pyplot as plt
import numpy as np
from rotations import *
from typing import List

plotting_space = np.linspace(0, 1.4 * 6, 1_000)
center = (5, 5)
rotation_rate = 1 # One revolution per second.


initial_vertices = [np.array([2, 2]), np.array([2, 8]), np.array([8, 8]), np.array([8, 2])]


def rotate_vectors(vectors:List[np.array],center:np.array,angle:float) -> List[np.array]:
    rotated_vectors = []
    for point in vectors:
        rotated_point = rotate_point(point-center,angle) + center
        rotated_vectors.append(
            rotated_point
        )
    return rotated_vectors

def main(initial_vertices:np.array):
        i = 0
        fig,ax = plt.subplots()
        ax.set_ylim(0,10)
        ax.set_xlim(0,10)

        while True:
            try:
                x1,y1 = initial_vertices[0]
                x2,y2 = initial_vertices[1]
                x3,y3 = initial_vertices[2]
                x4,y4 = initial_vertices[3]
                ax.plot([x1,x2],[y1,y2], color = 'blue')
                ax.plot([x2,x3],[y2,y3], color = 'blue')
                ax.plot([x3,x4],[y3,y4], color = 'blue')
                ax.plot([x4,x1],[y4,y1], color = 'blue')
                frequency = 2*np.pi*rotation_rate
                initial_vertices = rotate_vectors(initial_vertices,center,i * frequency)
                i+= .1
                plt.pause(0.01)
                plt.show()
            except KeyboardInterrupt:
                break


main(initial_vertices)