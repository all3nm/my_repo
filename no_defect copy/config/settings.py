"""Application configuration."""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    """Application settings."""

    database_name: str
    log_level: str


def get_settings() -> Settings:
    """Load application settings."""

    return Settings(
        database_name=os.getenv(
            "DATABASE_NAME",
            "employee.db",
        ),
        log_level=os.getenv(
            "LOG_LEVEL",
            "INFO",
        ),
    )