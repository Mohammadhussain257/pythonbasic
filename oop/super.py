class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('Name : ', self.name)
        print('Age : ', self.age)


class Student(Person):
    def __init__(self, name, age, rollNo, marks):
        # to invoked parent class constructor and method super() can be use
        super().__init__(name, age)
        self.rollNo = rollNo
        self.marks = marks

    def display(self):
        super().display()
        print('Roll No :', self.rollNo)
        print('Marks : ', self.marks)


class Teacher(Person):
    def __init__(self, name, age, salary, subject):
        super().__init__(name, age)
        self.salary = salary
        self.subject = subject

    def display(self):
        super().display()
        print('Salary : ', self.salary)
        print('Subject : ', self.subject)


s = Student('John Doe', 20, 101, 90)
t = Teacher('Sam Smith', 45, 120000, 'Python')
s.display()
print('*' * 20)
t.display()
