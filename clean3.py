def chunk(items, size):
    """Split items into chunks of at most size."""
    return [items[i:i + size] for i in range(0, len(items), size)]
