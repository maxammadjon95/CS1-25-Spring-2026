class Employee:
    def __init__(self, id: int, salary: int):
        self.id = id
        self.salary = salary

    def get_info(self) -> str:
        return f"EmployeeID:{self.id} Salary:{self.salary}"


class SalesEmployee(Employee):
    def __init__(self, id: int, salary: int, sales: int = 0):
        super().__init__(id, salary)
        self.sales = sales

    def get_info(self) -> str:
        return f"EmployeeID:{self.id} Salary:{self.salary} Sales:{self.sales}"


if __name__ == "__main__":
    id = 103
    salary = 70000
    sales = 300

    emp = Employee(id, salary)
    sales_emp = SalesEmployee(id, salary, sales)

    print(emp.get_info())
    print(sales_emp.get_info())