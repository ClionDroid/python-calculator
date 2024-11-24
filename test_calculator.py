import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    #add
    def test_add(self):
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.add(2, 3), 5)

    #subtract
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(3, 2), 1)

    #multiply
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(1, 2), 2)
        self.assertEqual(self.calc.multiply(3, 2), 6)

    #divide
    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(4, 2), 2)

    #modulo
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(9, 2), 1)
        self.assertEqual(self.calc.modulo(9, 5), 4)


if __name__ == '__main__':
    unittest.main()