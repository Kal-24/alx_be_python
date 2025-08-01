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
