class Outer:
    def __init__(self):
        print('Outer class constructor')

    class Inner:
        def __init__(self):
            print('Inner class  constructor')

        def m1(self):
            print('Inner class method')


o = Outer()
i = o.Inner()
i.m1()
print('*' * 20)
# or
i = Outer().Inner()
i.m1()
