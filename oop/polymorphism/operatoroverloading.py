# python does support operator overloading

class Book:
    def __init__(self, pages):
        self.pages = pages

    # inbuilt helper method for operator overloading
    def __add__(self, other):
        return self.pages + other.pages


# two object property is possible to add due to built in operator overloading
b1 = Book(700)
b2 = Book(12)
print('Total number of pages : ', b1 + b2)


class Books:
    def __init__(self, noofpage):
        self.noofpage = noofpage

    def __str__(self):
        return 'Total number of pages : ' + str(self.noofpage)

    def __add__(self, other):
        total = self.noofpage + other.noofpage
        book = Books(total)
        return book


b = Books(200)
bb = Books(300)
bbb = Books(400)
bbbb = Books(500)
print(b + bb + bbb + bbbb)


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks


s1 = Student('John', 100)
s2 = Student('Dow', 200)
print(s1 < s2)
