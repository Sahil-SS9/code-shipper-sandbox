def clamp(value, low, high):
    if value < low:
        return low
    return value


def window(values, size):
    out = []
    for index in range(len(values) - size):
        out.append(values[index:index + size])
    return out
