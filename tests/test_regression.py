import unittest
import numpy as np
from goph420_lab03 import regression as rgr


class TestRegression(unittest.TestCase):

    def test_Regression(self):
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
        self.assertAlmostEqual(a[0], 22.876, 3)
        self.assertAlmostEqual(a[1], 0.3277, 3)
        self.assertAlmostEqual(a[2], -0.1, 3)
        self.assertAlmostEqual(a[3], 0.0027, 3)
        self.assertAlmostEqual(rsq, 0.9768, 3)

        y = np.array([18, 3])
        Z = np.array([[2, 3],
                      [1, -1]])
        a, e, rsq = rgr.multi_regress(y, Z)
        self.assertAlmostEqual(a[0], 5.4, 3)
        self.assertAlmostEqual(a[1], 2.4, 3)
        self.assertAlmostEqual(rsq, 1.0, 3)

    def test_Regression_raises(self):
        y = np.array([18])
        Z = np.array([[2, 3],
                      [1, -1]])
        self.assertRaises(ValueError, rgr.multi_regress, y, Z)

        y = np.array([18, 3])
        Z = np.array([[2, 3],
                      [1, -1],
                      [5, 6]])
        self.assertRaises(ValueError, rgr.multi_regress, y, Z)


if __name__ == '__main__':
    unittest.main()
