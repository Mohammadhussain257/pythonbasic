number = int(input('Enter a number : '))
factorial = 1
count = 1

if number == 0:
    print('factor of {} is {} :'.format(number, 1))
else:
    while count < number:
        factorial *= count
        count += 1
    print('factor of {} is {} :'.format(number, factorial))
