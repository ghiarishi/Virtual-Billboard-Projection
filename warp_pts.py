import numpy as np
from est_homography import est_homography


def warp_pts(X, X_prime, interior_pts):
    """
    First compute homography from video_pts to logo_pts using X and X_prime,
    and then use this homography to warp all points inside the soccer goal

    Input:
        X: 4x2 matrix of (x,y) coordinates of goal corners in video frame
        X_prime: 4x2 matrix of (x,y) coordinates of logo corners in penn logo
        interior_pts: Nx2 matrix of points inside goal
    Returns:
        warped_pts: Nx2 matrix containing new coordinates for interior_pts.
        These coordinate describe where a point inside the goal will be warped
        to inside the penn logo. For this assignment, you can keep these new
        coordinates as float numbers.

    """

    # You should Complete est_homography first!
    H = est_homography(X, X_prime)

    ##### STUDENT CODE START #####

    new_col = np.ones((len(interior_pts), 1))
    interior_pts = np.hstack((interior_pts, new_col))

    interior_pts = np.transpose(interior_pts)
    warped_pts = np.matmul(H, interior_pts)

    lambda_ = warped_pts[2:]

    warped_pts = warped_pts/lambda_

    warped_pts = warped_pts[:2]
    warped_pts = np.transpose(warped_pts)


    ##### STUDENT CODE END #####

    return warped_pts