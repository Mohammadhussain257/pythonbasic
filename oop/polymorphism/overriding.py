class Parent:
    def property(self):
        print("Parent property")

    def marry(self):
        print("Arrange marriage")


class Child(Parent):
    # Child class can re-define parent class method
    def marry(self):
        # if parent method need to call then
        super().marry()
        print("Love marriage")


c = Child()
c.property()
c.marry()
