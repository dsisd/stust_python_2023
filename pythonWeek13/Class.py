class Employee:
    #Constructor to initialize employee attributes
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name 
        self.emp_salary = emp_salary
        self.emp_department = emp_department 

    #Method to calculate hours worked if is more than 50, the method computes overtime and adds it to the salary. 
    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            salary = self.emp_salary + (overtime * (self.emp_salary / 50))
            return salary
        else:
            salary = self.emp_salary
            return salary

    #Method to Assign New Departmen
    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    #Method to Print Employee Details
    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: ${self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")

#sample data
employee1 = Employee("E7876", "ADAMS", 50000, "ACCOUNTING")
employee2 = Employee("E7499", "JONES", 45000, "RESEARCH")
employee3 = Employee("E7900", "MARTIN", 50000, "SALES")
employee4 = Employee("E7698", "SMITH", 55000, "OPERATIONS")
#sample to change department
employee1.emp_assign_department("HR")
employee1.print_employee_details()
#sample to calculate salary by total worktime
total_salary_employee2 = employee2.calculate_emp_salary(55)
print(f"Total Salary for {employee2.emp_name}: ${total_salary_employee2}")