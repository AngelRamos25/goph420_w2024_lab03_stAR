import numpy as np
import matplotlib as plt
from goph420_lab03 import regression as rgr


def main():

    t, y = np.loadtxt('M_data.txt', float, unpack=True)
    # a, e, rsq = rgr.multi_regress(y, Z)

    plt.plot(t, y)
    plt.show()


if __name__ == "__main__":
    main()
