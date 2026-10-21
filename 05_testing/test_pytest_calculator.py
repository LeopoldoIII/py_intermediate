"""
Demonstrates modern testing patterns with pytest (and unittest fallback):
- Fixtures
- Parameterized test cases
- Exception testing
"""

import unittest

try:
    from .calc import add, subtract, multiply, divide, power
except ImportError:
    from calc import add, subtract, multiply, divide, power

class TestCalculatorPatterns(unittest.TestCase):

    def setUp(self):
        self.sample_numbers = {"a": 10.0, "b": 5.0}

    def test_fixture_pattern(self):
        self.assertEqual(add(self.sample_numbers["a"], self.sample_numbers["b"]), 15.0)
        self.assertEqual(subtract(self.sample_numbers["a"], self.sample_numbers["b"]), 5.0)

    def test_parametrized_multiplication(self):
        cases = [
            (2, 3, 6),
            (-1, 5, -5),
            (0, 100, 0),
            (2.5, 2, 5.0),
        ]
        for x, y, expected in cases:
            with self.subTest(x=x, y=y):
                self.assertEqual(multiply(x, y), expected)

    def test_parametrized_division(self):
        cases = [
            (10, 2, 5.0),
            (-9, 3, -3.0),
            (5, 2, 2.5),
        ]
        for x, y, expected in cases:
            with self.subTest(x=x, y=y):
                self.assertEqual(divide(x, y), expected)

    def test_divide_by_zero_exception(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 4), 16)
        self.assertEqual(power(9, 0.5), 3.0)

if __name__ == "__main__":
    unittest.main()
