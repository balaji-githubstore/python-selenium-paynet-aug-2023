class Employee:
    # static variable or class variable
    company_name = None
    company_location = "Malaysia"

    # non-static variable or instance variable
    def __init__(self,id=None):
        self.emp_id = id
        self.emp_name = None
        self.emp_salary = None
        self.performance = None
        print("Launch browser")

    @staticmethod
    def get_author_name():
        return "Balaji Dinakaran"

    @staticmethod
    def print_company_details():
        print(f"Company Name: {Employee.company_name}")
        print(f"Company Location: {Employee.company_location}")

    def print_employee_detail(self):
        print("-" * 50)
        print(f"Employee Id: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Performance: {self.performance}")
        print("-" * 50)

    def allocate_performance(self):
        if self.performance == "A":
            print("allocate 1000")
            self.emp_salary = self.emp_salary + 1000
        elif self.performance == "B":
            print("allocate 500")
            self.emp_salary = self.emp_salary + 500
        else:
            print("allocate 100")
            self.emp_salary = self.emp_salary + 100


    @property
    def print_welcome_message(self):
        return f"Hi {self.emp_name}, Welcome to the company!!!"
