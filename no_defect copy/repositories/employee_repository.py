"""Employee repository."""

from typing import Any
import sqlite3


class EmployeeRepository:
    """Employee data access."""

    def find_by_id(
        self,
        employee_id: int,
    ) -> dict[str, Any] | None:
        """
        Retrieve employee from database.

        Args:
            employee_id: Employee identifier.

        Returns:
            Employee dictionary or None.
        """

        query = """
            SELECT
                id,
                name
            FROM employees
            WHERE id = ?
        """

        with sqlite3.connect(
            "employee.db"
        ) as connection:

            cursor = connection.execute(
                query,
                (employee_id,),
            )

            row = cursor.fetchone()

        if row is None:
            return None

        return {
            "id": row[0],
            "name": row[1],
        }