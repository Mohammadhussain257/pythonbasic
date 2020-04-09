class P1:
    def m1(self):
        print('Parent 1 Method')


class P2:
    def m2(self):
        print('Parent 2 Method')


class C(P1, P2): pass


# in python in multiple inheritance method resolution is always based on order of parent
c = C()
c.m1()
c.m2()
