import numpy as np
from goph420_lab03 import regression as rgr


def main():
    y = np.array([22.8, 22.8, 22.8, 20.6, 13.9, 11.7, 11.1, 11.1])
    Z = np.array([[1,	0,	0,	0],
                  [1,	2.3,	5.29,	12.167],
                  [1,	4.9,	24.01,	117.649],
                  [1,	9.1,	82.81,	753.571],
                  [1,	13.7,	187.69,	2571.353],
                  [1,	18.3,	334.89,	6128.487],
                  [1,	22.9,	524.41,	12008.989],
                  [1,	27.2,	739.84,	20123.648]])

    a, e, rsq = rgr.multi_regress(y, Z)

    t, v = np.loadtxt('s_wave_data.txt', float, unpack=True)


if __name__ == "__main__":
    main()
