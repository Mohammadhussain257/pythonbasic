class Employee:
    # constructor
    def __init__(self, empnum, empname, empsalary):
        self.empnum = empnum
        self.empname = empname
        self.empsalary = empsalary

    # instance method
    def display(self):
        print('Employee Number : ', self.empnum)
        print('Employee Name  : ', self.empname)
        print('Employee Salary : ', self.empsalary)


class Test:
    # static method
    def modify(emp):
        emp.empsalary = emp.empsalary + 1000
        emp.display()


e = Employee(121, 'Doe', 70000)
Test.modify(e)
