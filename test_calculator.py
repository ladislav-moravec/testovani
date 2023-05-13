from unittest import TestCase

from calculator import Calculator


class TestCalculator(TestCase):

    def test_to_the_power_of(self):
        calc = Calculator()

        self.assertEqual(4, calc.to_the_power_of(2, 2))
        self.assertEqual(9, calc.to_the_power_of(3, 2))
        self.assertNotEqual(4, calc.to_the_power_of(3, 3))

    def test_add(self):
        calc = Calculator()

        self.assertEqual(4, calc.add(2, 2))
        self.assertEqual(14, calc.add(9, 5))
        self.assertNotEqual(4, calc.add(2, 4))

    def test_reduce(self):
        calc = Calculator()

        self.assertEqual(4, calc.reduce(6, 2))
        self.assertEqual(89140, calc.reduce(89150, 10))
        self.assertNotEqual(4258390, calc.reduce(323, 4895479802))

    def test_div(self):
        calc = Calculator()

        self.assertEqual(4, calc.div(16, 4))
        self.assertEqual(2, calc.div(160, 80))
        self.assertNotEqual(2, calc.div(2324, 424))
