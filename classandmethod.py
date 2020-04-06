class ClassAndMethod:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # user define method
    def display(self):
        print('Your name is : ', self.name)
        print('Your age is : ', self.age)


name = input('Enter your name : ')
age = int(input('Enter your age : '))
# object creation
obj = ClassAndMethod(name, age)
# calling method
obj.display()
