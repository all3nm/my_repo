"""User data access operations."""

from typing import Any


class userrepository:

    def find_by_id(self, user_id: int):
        """Find a user by identifier."""
        users = {1: {"id": 1, "name": "Sample User"}}
        return users.get(user_id)
