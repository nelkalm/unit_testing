import unittest

from numpy import union1d
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        # run the add function, we can run more edge cases
        # in the same add function.
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        # run the subtract function, we can run more edge cases
        # in the same add function.
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        # run the multiply function, we can run more edge cases
        # in the same add function.
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        # run the divide function, we can run more edge cases
        # in the same add function.
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)
        
        # Testing Exception 2 ways:
        # (1) assertRaises
        # self.assertRaises(ValueError, calc.divide, 10, 0)
        # (2) Use a context manager:
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
