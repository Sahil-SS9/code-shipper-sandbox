def slugify(text):
    """Lowercase words joined by hyphens."""
    return "-".join(text.lower().split())
