# Define a class for Employee
class Employee:
    def __init__(self, name, salary, deductions):
        self.name = name
        self.salary = salary
        self.deductions = deductions

    def calculate_net_salary(self):
        return self.salary - self.deductions

# Define a function to generate payslip
def generate_payslip(employee):
    print("Payslip for:", employee.name)
    print("Gross Salary:", employee.salary)
    print("Deductions:", employee.deductions)
    print("Net Salary:", employee.calculate_net_salary())

# Define a function to generate payroll
def generate_payroll(employees):
    with open("payroll.txt", "a") as file:
        for employee in employees:
            filename = employee.name
            f = open('payslip/'+filename+'.txt', 'w')
            file.write("Payslip for: " + employee.name + "\n")
            file.write("Gross Salary: " + str(employee.salary) + "\n")
            file.write("Deductions: " + str(employee.deductions) + "\n")
            file.write("Net Salary: " + str(employee.calculate_net_salary()) + "\n\n")
            f.write("Payslip for: " + employee.name + "\n")
            f.write("Gross Salary: " + str(employee.salary) + "\n")
            f.write("Deductions: " + str(employee.deductions) + "\n")
            f.write("Net Salary: " + str(employee.calculate_net_salary()) + "\n\n")


def display_payslip():
    with open("payroll.txt", "r") as file:
        out = file.read()
        print(out)

def display_payment(name):
    with open("payslip/"+name+".txt", "r") as file:
        out = file.read()
        print(out)



# Accept staff details from users
def accept_staff_details():
    employees = []
    num_staff = int(input("Enter number of staff: "))
    for i in range(num_staff):
        name = input("Enter name: ")
        salary = float(input("Enter salary: "))
        deductions = float(input("Enter deductions: "))
        employee = Employee(name, salary, deductions)
        employees.append(employee)
    return employees

# Main program
def main():
    while True:
        print("1. Add Employee\n2. Display Employee Payslip\n3. Display All Payroll\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            employees = accept_staff_details()
            generate_payroll(employees)
            print("Payroll generated successfully!")
        elif choice == "2":
            print()
            display_payslip()
        elif choice == "3":
            name = input("Enter Employee's Name: ")
            display_payment(name)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")



if __name__ == "__main__":
    main()
