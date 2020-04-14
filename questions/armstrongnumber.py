number = int(input('Enter number :'))
sum = 0
temp = number

if number == -1:
    print('Please enter positive number : ')

while number > 0:
    remainder = number % 10
    sum += remainder**3
    number //= 10

if sum == temp:
    print(temp, ' is an Armstrong number')
else:
    print(temp, ' is not an Armstrong number')