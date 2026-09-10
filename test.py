def MAIN() -> None:
    """Run the application."""
    service = User_Service()
    print(service.getDisplayName(1))


if __name__ == "__main__":
    MAIN()
