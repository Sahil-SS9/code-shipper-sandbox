"""Small arithmetic helpers used by Code-Shipper's sandbox."""


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("b must not be zero")
    return a / b


def mean(values):
    return sum(values) / len(values)


def clamp(value, low, high):
    return max(low, min(high, value))
