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