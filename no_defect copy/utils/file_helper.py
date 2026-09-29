"""File utility functions."""

from pathlib import Path
from typing import Any
import json


def save_json_file(
    file_path: str,
    data: dict[str, Any],
) -> None:
    """
    Save JSON data.

    Args:
        file_path: Destination file.
        data: Data dictionary.
    """

    path = Path(file_path)

    with path.open(
        "w",
        encoding="utf-8",
    ) as file_handle:

        json.dump(
            data,
            file_handle,
            indent=4,
        )