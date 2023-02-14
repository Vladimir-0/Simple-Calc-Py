from decimal import Decimal
from math import log
from typing import Union


_func = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '**': lambda a, b: a ** b,     # Pow
    '√': lambda a, b: a ** 1 / b,  # Root
    '//': lambda a, b: a // b,     # Div
    '%': lambda a, b: a % b,       # Mod

    '<': lambda a, b: a < b,
    '>': lambda a, b: a > b,
    '<=': lambda a, b: a <= b,
    '>=': lambda a, b: a >= b,
    '==': lambda a, b: a == b,
    '!=': lambda a, b: a != b,

    'log': lambda a, b: log(a, b)
}

operations = tuple(_func.keys())


def perform_operation(a: Decimal, b: Decimal, operation: str) -> Union[Decimal, str]:
    """
    Performs operation on 2 numbers.
    :param a: First argument.
    :param b: Second argument.
    :param operation: Operation type.
    :return: The calculation result.
    """
    try:
        result = _func[operation](a, b)
    except KeyError:
        return "Incorrect operation"
    return result
