import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1000, 500), -500)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(-1000, 500), -1500)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2 ,3), 6)
        self.assertEqual(mul(-4, 5), -20)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10, 2), 5)
        self.assertAlmostEqual(div(7, 2), 3.5)
        self.assertEqual(div(-9, 3), -3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertEqual(logarithm(2, 256), 8)
        self.assertEqual(logarithm(10321904, 1), 0)
        self.assertAlmostEqual(logarithm(2, 3.5), 1.8073549)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(0, 1)

    def test_log_invalid_argument(self):
          with self.assertRaises(ValueError):
              logarithm(-1, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(16), 4)
        with self.assertRaises(ValueError):
            square_root(-4)

if __name__ == "__main__":
    unittest.main()