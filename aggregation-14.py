class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_employee_info(self):
        return f"Employee Name: {self.name}, Position: {self.position}" 
    
class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee

    def get_department_info(self):
        return f"Depatment: {self.department_name}, Employee: {self.employee.get_employee_info()}"
    


employee1 = Employee("Khansa Rahman", "Website Developer")
department1 = Department("IT Department", employee1)

print(department1.get_department_info())
