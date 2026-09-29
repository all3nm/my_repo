"""Application entry point."""

from services.employee_service import EmployeeService


def main() -> None:
    """Run the application."""
    service = EmployeeService()

    employee = service.get_employee(1)

    if employee:
        print(employee["name"])
    else:
        print("Employee not found")


if __name__ == "__main__":
    main()