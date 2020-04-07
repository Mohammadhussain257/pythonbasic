class GetterSetter:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age


name = input('Enter your name : ')
age = input('Enter your age : ')

gs = GetterSetter()
gs.setName(name)
gs.setAge(age)
print(gs.getName())
print(gs.getAge())
