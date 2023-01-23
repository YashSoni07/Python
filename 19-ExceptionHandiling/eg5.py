class EmployeeSalary(Exception):

    def userSalary(self, eSalary):
        if eSalary < 5000:
            raise Exception("Salary is less then 5000")
        else:
            print("Your Salary is ", eSalary)


EmployeeSalary().userSalary(4000)