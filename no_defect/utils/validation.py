"""Validation helpers."""


def is_positive_integer(
    value: int,
) -> bool:
    """
    Check if value is positive.

    Args:
        value: Number to validate.

    Returns:
        True if positive.
    """
    return value > 0