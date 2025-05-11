class Employee:
    name = "Khansa"
    _salary = 60000
    __ssn = "123--6666-99"

emp = Employee()
print("Name:", emp.name)
print("Salary:", emp._salary)

try:
    print("SSN:", emp.__ssn)
except AttributeError as e:
    print("Error:", e)    


print("SSN (via name mangling): ", emp._Employee__ssn)

