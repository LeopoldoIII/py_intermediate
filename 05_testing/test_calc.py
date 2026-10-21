import unittest

try:
    from . import calc
except ImportError:
    import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-5, -5), -10)
        self.assertAlmostEqual(calc.add(0.1, 0.2), 0.3, places=7)

    def test_subtract(self):
        self.assertEqual(calc.subtract(20, 10), 10)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(5, 10), -5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(3, 7), 21)
        self.assertEqual(calc.multiply(-2, 4), -8)
        self.assertEqual(calc.multiply(0, 100), 0)
        # Test backward-compatible alias
        self.assertEqual(calc.multipy(5, 5), 25)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertEqual(calc.divide(-10, 2), -5)
        self.assertEqual(calc.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)

    def test_power(self):
        self.assertEqual(calc.power(2, 3), 8)
        self.assertEqual(calc.power(5, 0), 1)

if __name__ == '__main__':
    unittest.main()
