"""Formatting utilities."""


def format_name(first_name: str, last_name: str) -> str:
    """Return a normalized full name."""
    return f"{first_name.strip()} {last_name.strip()}"
