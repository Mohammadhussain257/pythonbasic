number = int(input('Enter number : '))
count = 0
counter = 1
while counter <= number:
    if number % counter ==0:
        count +=1
    counter +=1

if count == 2:
    print(number, ' is a prime')
else:
    print(number, 'is not a prime')