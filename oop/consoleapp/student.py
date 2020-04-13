class Student:
    def __init__(self, name, percent):
        self.name = name
        self.percent = percent

    def display(self):
        print('Hi', self.name)
        print('Your percent is :', self.percent)

    def grade(self):
        if self.percent >= 60:
            print('First Grade')
        elif self.percent >= 50:
            print('Second Grade')
        elif self.percent >= 35:
            print('Third Grade')
        else:
            print('Your are failed')


n = int(input('Enter number of student : '))
for i in range(n):
    name = input('Enter student name : ')
    percent = int(input('Enter student percent : '))
    s = Student(name, percent)
    s.display()
    s.grade()
    print('*' * 20)
