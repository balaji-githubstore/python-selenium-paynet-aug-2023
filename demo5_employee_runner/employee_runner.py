from demo4_employees.employee_module import Employee

print(Employee.company_name)
print(Employee.company_location)

Employee.company_name="CGI"

print(Employee.company_name)
print(Employee.company_location)

emp1=Employee()
# emp1.emp_id=101
emp1.emp_name="Saul"
emp1.emp_salary=7800.50
emp1.performance="A"


emp2=Employee(1002)
emp2.emp_id=102
emp2.emp_name="kim"
emp2.emp_salary=9000
emp2.performance="B"


name=Employee.get_author_name()
print(name)

Employee.print_company_details()
print(type(emp1))



emp1.print_employee_detail()
emp2.print_employee_detail()

emp1.allocate_performance()
emp2.allocate_performance()

emp1.print_employee_detail()
emp2.print_employee_detail()


print(emp1.print_welcome_message)