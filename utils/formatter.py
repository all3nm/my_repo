"""Formatting utilities."""


def format_name(FirstName: str, lastName: str) -> str:
    """Return a normalized full name."""
    return f"{FirstName.strip()} {lastName.strip()}"
