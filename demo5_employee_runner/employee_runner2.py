from demo4_employees import employee_module

print(employee_module.Employee.company_name)
print(employee_module.Employee.company_location)

employee_module.Employee.company_name="CGI"

print(employee_module.Employee.company_name)
print(employee_module.Employee.company_location)

emp1=employee_module.Employee()
emp1.emp_id=101
emp1.emp_name="Saul"
emp1.emp_salary=7800.50
emp1.performance="A"




