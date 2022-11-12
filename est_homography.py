import numpy as np
from scipy.linalg import null_space


def est_homography(X, X_prime):
    """
    Calculates the homography of two planes, from the plane defined by X
    to the plane defined by X_prime. In this assignment, X are the coordinates of the
    four corners of the soccer goal while X_prime are the four corners of the penn logo

    Input:
        X: 4x2 matrix of (x,y) coordinates of goal corners in video frame
        X_prime: 4x2 matrix of (x,y) coordinates of logo corners in penn logo
    Returns:
        H: 3x3 homogeneous transformation matrix s.t. X_prime ~ H*X

    """

    ##### STUDENT CODE START #####
    x_prime = [X_prime[0][0], X_prime[1][0], X_prime[2][0], X_prime[3][0]]
    y_prime = [X_prime[0][1], X_prime[1][1], X_prime[2][1], X_prime[3][1]]
    x = [X[0][0], X[1][0], X[2][0], X[3][0]]
    y = [X[0][1], X[1][1], X[2][1], X[3][1]]

    A = []
    for i in range(4):
        A.append([-x[i], -y[i], -1, 0, 0, 0, x[i] * x_prime[i], y[i] * x_prime[i], x_prime[i]])
        A.append([0, 0, 0, -x[i], -y[i], -1, x[i] * y_prime[i], y[i] * y_prime[i], y_prime[i]])

    ns = null_space(A)
    print(ns)
    [U, S, Vt] = np.linalg.svd(A)

    H = np.array(Vt[-1])
    H = np.array(H, dtype=np.float32)
    H = H.reshape(3, 3)

    ##### STUDENT CODE END #####

    return H


x = [[0, 0], [1, 1], [0, 5], [1, 5]]
x_prime = [[0, 0], [1, 1], [0, 5], [1, 5]]
print(est_homography(x, x_prime))

