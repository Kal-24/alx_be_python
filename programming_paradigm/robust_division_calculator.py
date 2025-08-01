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


# Standalone function for compatibility with imports expecting a function
def safe_divide(numerator, denominator):
    calculator = SimpleCalculator()
    return calculator.safe_divide(numerator, denominator)
