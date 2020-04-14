number = int(input('Enter number :'))
temp = 0
result = 0
while number != 0:
    temp = number % 10
    result = (result*10)+temp
    number //= 10

print(result)