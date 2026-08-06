import pytest

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

@pytest.fixture

def calculator() -> Calculator :
    """Provide a fresh Calculator instance for each test"""
    return Calculator()

def test_add(calculator:Calculator) -> None:
    """Adding 5 and 3 should give us  a result of 8"""
    calculator.add(5)
    calculator.add(3)
    assert calculator.value == 8


def test_subtract(calculator:Calculator) -> None:
    """Subtracting 4 from 10 should give us 6"""
    calculator.add(10)
    calculator.subtract(4)
    assert calculator.value == 6

def test_multiply(calculator:Calculator) -> None:
    """Multiplying 7 by 6 should give us 42"""
    calculator.add(7)
    calculator.multiply(6)
    assert calculator.value == 42

def test_divide(calculator:Calculator) -> None:
    """Multiplying 7 by 6 should give us 42"""
    calculator.add(20)
    calculator.divide(4)
    assert calculator.value == 5


def test_divide_by_zero_raises_error(calculator:Calculator) -> None:
    """Divide by zero should raise an error"""
    with pytest.raises(ValueError):
        calculator.divide(0)

def test_divide_by_zero_error_message(calculator:Calculator) -> None:
    """Divide by zero should raise an error"""
    with pytest.raises(ValueError, match="cannot Divide by zero"):
        calculator.divide(0)


# testing 7 rows in one place

@pytest.mark.parametrize(
    "initial, operation, operand, expected",
    [
        (10, "add", 5, 15),
        (10, "subtract", 4, 6),
        (7, "multiply", 6, 42),
        (20, "divide", 4, 5),
        (0, "add", 100, 100),
        (100, "subtract", 100, 0),
        (2, "multiply", 0, 0)

    ],
)

def test_arithmetic_operation(
        initial: float,
        operation: str,
        operand: float,
        expected: float,
) -> None:
    """Parametrized test covering add, subtract, multiply and divide operations"""
    calc: Calculator = Calculator(initial_values=initial)

    if operation == "add":
        calc.add(operand)
    elif operation == "subtract":
        calc.subtract(operand)
    elif operation == "multiply":
        calc.multiply(operand)
    elif operation == "divide":
        calc.divide(operand)

    assert calc.value == expected

@pytest.mark.parametrize(
    "starting_value",
    [0,1,100,-50,3.14],
)

def test_divide_by_zero_always_raises(starting_value: float) -> None:
    """Dividing by zero should raise a ValueError no matter what the current values is."""
    calc: Calculator = Calculator(initial_values=starting_value)
    with pytest.raises(ValueError):
        calc.divide(0)

def test_initial_value(calculator:Calculator) -> None:
    """A new Calculator should start with a value of 0."""
    assert calculator.value == 0

def test_reset(calculator:Calculator) -> None:
    """After adding 100, calling reset() should set the value back to 0."""
    calculator.add(100)
    calculator.reset()
    assert calculator.value == 0


def test_custom_initial_value() -> None:
    """Creating na Calculator with an initial value of 42 should at 42"""
    calc: Calculator = Calculator(initial_values=42)
    assert calc.value == 42


@pytest.mark.parametrize(
    "initial, operations, expected",
    [
        (0, [("add", 10), ("multiply", 3), ("subtract", 5), ("divide", 5)], 5),
        (0, [("add", 10), ("add", 3), ("add", 5)], 18),
        (100, [("subtract", 50), ("divide", 2)], 25),
        (2, [("multiply", 3), ("multiply", 4)], 24)
    ]
)
def test_chain_operations(
        initial: float,
        operations: list[tuple[str, float]],
        expected: float,
) -> None:
    """Parametrized test verifying that  chained operations produce the correct final value. """
    calc: Calculator = Calculator(initial_values=initial)

    for op_name, operand in operations:
        if op_name == "add":
            calc.add(operand)
        elif op_name == "subtract":
            calc.subtract(operand)
        elif op_name == "multiply":
            calc.multiply(operand)
        elif op_name == "divide":
            calc.divide(operand)

    assert calc.value == expected

    #run -> pytest filename.py -v