class Test:

    @staticmethod
    def sum(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def average(x, y):
        return (x + y) / 2


print('sum is : ', Test.sum(4, 5))
print('sum is : ', Test.sub(4, 5))
print('sum is : ', Test.multiply(4, 5))
print('sum is : ', Test.average(4, 5))
