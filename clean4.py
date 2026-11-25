def mean(values):
    """Arithmetic mean."""
    if not values:
        raise ValueError("mean of empty sequence")
    return sum(values) / len(values)
