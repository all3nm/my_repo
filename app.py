"""Application entry point."""

from services.user_service import UserService


def main() -> None:
    """Run the application."""
    service = UserService()
    print(service.getDisplayName(1))


if __name__ == "__main__":
    main()
