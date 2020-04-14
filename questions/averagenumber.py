number = int(input('Enter nth number to calculate average : '))
sum =0
for i in range(number):
    numbers = float(input('Enter number : '))
    sum +=numbers

average = sum/number
print(f"Average of total number is :{average}")