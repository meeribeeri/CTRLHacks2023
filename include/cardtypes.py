from enum import Enum

class MathType(Enum):
    OPERATOR = 0
    VALUE = 1
    EXPONENT = 2
    PARANTHESIS = 3
    VARIABLE = 4