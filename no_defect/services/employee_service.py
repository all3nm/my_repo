"""Employee business logic."""

from typing import Any

from repositories.employee_repository import EmployeeRepository


class EmployeeService:
    """Employee operations."""

    def __init__(self) -> None:
        self._repository = EmployeeRepository()

    def get_employee(
        self,
        employee_id: int,
    ) -> dict[str, Any] | None:
        """
        Retrieve employee details.

        Args:
            employee_id: Employee identifier.

        Returns:
            Employee information or None.
        """
        return self._repository.find_by_id(
            employee_id
        )