class Test:
    # syntax for creating constructor
    def __init__(self):
        print('No-agrs')

    # constructor overloading concept is not available in python so most latest one will be called
    def __init__(self, x):
        print('One-args')


# t1 =  Test() gives error positional argument
t2 =  Test(20)