# python won't support method overloading and constructor overloading
# because we cannot define type explicitly
# if it is required then do it in this way

class Test:
    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            print(a + b + c)
        elif a != None and b != None:
            print(a + b)
        else:
            print('Please privide 2 or three arguments')

    # in a concise form
    def add(self, *x):
        total = 0
        for number in x:
            total += number
        print('The sum is : ', total)

    # for constructor
    def __init__(self, *a):
        print('Any number of argument supported including zero')


t = Test()
t.sum(10, 10, 10)
t.sum(10, 10)
t.sum(10)
t.add(100, 10)
t.add(100, 300, 12)
