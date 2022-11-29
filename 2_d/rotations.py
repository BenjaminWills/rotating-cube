import numpy as np


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
    return np.array([[cosine, -sine], [sine, cosine]])


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
