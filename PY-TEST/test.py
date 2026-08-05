#unittest -> TestCase subclass, setUp, self.assertEqual,
#   self.assertRaises with manual message extraction
#pytest -> plain functions, opt-in fixtures, plain assert,
#    pytest.raises with built-in match, parametrize

import unittest

class Calculator:
    """A basic calculator that stores a running total and supports
    add, subtract, multiply, and divide operations."""

    def __init__(self, initial_values:float = 0.0) -> None :
        self._value:float = initial_values

    @property
    def value(self) -> float :
        return self._value

    def add(self, amount: float) -> None:
        self._value += amount

    def subtract(self, amount: float) -> None:
        self._value -= amount

    def multiply(self, amount: float) -> None:
        self._value *= amount

    def divide(self, amount:float) -> None:
        if amount == 0:
            raise ValueError("cannot Divide by zero")
        self._value /= amount

    def reset(self) -> None:
        self._value = 0.0

class TestCalculator(unittest.TestCase): # ->testCalulator have to inherit unittest
    """Test for the calculator class unig Python's Build-in unitest module"""

    def setUp(self) -> None: #-> this method runs before every single test method
        """Create a fresh Calculator instance before each test"""
        self.calc: Calculator = Calculator()

    def test_add(self) -> None:
        """Adding 5 and 3 should give a result of 8"""
        self.calc.add(5)
        self.calc.add(3)
        self.assertEqual(self.calc.value, 8)

    def test_subtract(self) -> None:
        """Subtracting 4 from 10 should give a result of 6"""
        self.calc.add(10)
        self.calc.subtract(4)
        self.assertEqual(self.calc.value, 6)

    def test_multiply(self) -> None:
        """Multiplying 4 from add 10 should give a result of 40"""
        self.calc.add(10)
        self.calc.multiply(4)
        self.assertEqual(self.calc.value, 40)

    def test_devide(self) -> None:
        """Dividing 20 by 4 should give us 5."""
        self.calc.add(20)
        self.calc.divide(4)
        self.assertEqual(self.calc.value, 5)

    def test_divide_by_zero_raises_message(self) -> None:
        """Divide by zero should raise a ValueError"""
        with self.assertRaises(ValueError):
             self.calc.divide(0)

    def test_divide_bu_zero_error_message(self) -> None:
        """The ValueError should contain the message 'Cannot Divide by zero'"""
        with self.assertRaises(ValueError) as ctx: # -> ctx is contect and it will get what error name
            self.calc.divide(0)
        self.assertEqual("cannot Divide by zero", str(ctx.exception)) # ->  in there we check the str error value

    def test_chain_operation(self) -> None:
        """Chaining add, multiply, and subtract should give the correct final values."""
        self.calc.add(10)
        self.calc.multiply(3)
        self.calc.subtract(5)
        self.calc.divide(5)
        self.assertEqual(5, self.calc.value)

    def test_initial_values(self) -> None:
        """A new Calculator should start with a value of zero"""
        self.assertEqual(self.calc.value, 0.0)

    def test_reset(self) -> None:
        """After adding 100, calling reset() should set the value back to 0."""
        self.calc.add(100)
        self.calc.reset()
        self.assertEqual(self.calc.value, 0.0)

    def test_custom_initial_values(self) -> None:
        """Creating a Calculator with an initial value of 42 should start at 42"""
        calc: Calculator = Calculator(initial_values=42)
        self.assertEqual(calc.value, 42)


def main():
    unittest.main()

if __name__ == "__main__":
    main()