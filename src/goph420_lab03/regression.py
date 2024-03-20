import numpy as np


def multi_regress(y, Z):
    """ Perform multiple linear regression.

    Parameters.
    -----------------
    y: array_like, shape = (n,) or (n,1)
       The vector of dependent variable data
    z: array_like, shape = (n,m)
       The matrix of independent variable data

    Returns:
    ------------------
    numpy.ndarray, shape = (m,) or (m,1)
        The vector of model coefficients
    numoy.ndarray, shape = (n,) or (n,1)
        The vector of residuals
    float
        The coefficient of determination, R^2

    Raises:
    ------------------
    Value Error: Dimensions of y and Z are not consistent.


    """
    Ny = len(y)
    Nz = Z.shape[0]

    if Ny != Nz:
        raise ValueError("Number of data points is not the same at y and Z.")

    avg = np.sum(y)/len(y)
    avg_e = np.subtract(y, avg)
    avg_e = np.multiply(avg_e, avg_e)
    St = sum(avg_e)

    ZTZ = np.matmul(np.transpose(Z), Z)
    inv = np.linalg.inv(ZTZ)
    Zy = np.matmul(np.transpose(Z), y)
    a = np.matmul(inv, Zy)

    y_est = np.matmul(Z, a)
    e_r = np.subtract(y, y_est)
    e_r_sq = np.multiply(e_r, e_r)
    Sr = sum(e_r_sq)

    R2 = np.abs(St - Sr)/St
    R2 = np.round(R2, 3)

    return (a, e_r, R2)
