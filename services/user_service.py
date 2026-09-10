"""User-related business logic."""

from repositories.user_repository import userrepository


class UserService:
    """Provide user-related operations."""

    def __init__(self) -> None:
        self._repository = userrepository()

    def getDisplayName(self, user_id: int) -> str:
        """Return the display name for a user."""
        user = self._repository.find_by_id(user_id)
        if user is None:
            raise ValueError(f"User {user_id} was not found")
        return user["name"]
