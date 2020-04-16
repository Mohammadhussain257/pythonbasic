'''Question:
Write a program which can compute the square up to nth term of a given numbers in a key value pair.'''
number = int(input('Enter a number : '))
di = dict()
for i in range(1, number+1):
    di[i] = i*i
print(di)

