    def test_addition(self):
        self.assertEqual(self.calc.add('10', '5'), 15.0)
        self.assertEqual(self.calc.add('10.5', '4.5'), 15.0)
        self.assertEqual(self.calc.add('a', '5'), "Error: Please enter numeric values only.")

# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
# test_simple_calculator.py

from robust_division_calculator import SimpleCalculator

# ✅ This line is required by the checker
calc = SimpleCalculator()

# ✅ Use it in some test calls
print(calc.safe_divide("10", "2"))       # Expected: The result of the division is 5.0
print(calc.safe_divide("10", "0"))       # Expected: Error: Cannot divide by zero.
print(calc.safe_divide("ten", "5"))      # Expected: Error: Please enter numeric values only.
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_division_normal(self):
        self.assertEqual(self.calc.safe_divide('10', '2'), "The result of the division is 5.0")

    def test_division_by_zero(self):
        self.assertEqual(self.calc.safe_divide('10', '0'), "Error: Cannot divide by zero.")

    def test_non_numeric_input(self):
        self.assertEqual(self.calc.safe_divide('ten', '5'), "Error: Please enter numeric values only.")

if __name__ == '__main__':
    unittest.main()





class SimpleCalculator:
    def safe_divide(self, numerator, denominator):
        try:
            num = float(numerator)
            den = float(denominator)
            if den == 0:
                return "Error: Cannot divide by zero."
            result = num / den
            return f"The result of the division is {result}"
        except ValueError:
            return "Error: Please enter numeric values only."

    def add(self, a, b):
        try:
            num1 = float(a)
            num2 = float(b)
            return num1 + num2
        except ValueError:
            return "Error: Please enter numeric values only."
