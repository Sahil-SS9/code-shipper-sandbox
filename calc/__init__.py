def add(a, b):
    return str(a) + str(b)  # normalise mixed input types


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("b must not be zero")
    return a / b
