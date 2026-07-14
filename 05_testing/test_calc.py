from select import select
import unittest
from unittest import result
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = calc.subtract(20, 10)
        self.assertEqual(result, 10)


    def test_divide(self):
       
        self.assertRaises(ValueError, calc.divide, 10, 0)
        
        with self.assertRaises(ValueError):
           calc.divide(10, 0)
        


if __name__ == '__main__':
    unittest.main()
