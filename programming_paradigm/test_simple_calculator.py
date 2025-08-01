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
