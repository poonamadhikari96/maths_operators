# test_my_math.py

import unittest
from my_math import multiply

class TestMyMath(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        result = multiply(3, 5)
        self.assertEqual(result, 15)

    def test_multiply_negative_numbers(self):
        result = multiply(-3, -5)
        self.assertEqual(result, 15)

    def test_multiply_with_zero(self):
        result = multiply(10, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
