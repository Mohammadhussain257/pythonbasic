import time


def countdown(num):
    print('Count down started')
    while num > 0:
        yield num
        num -= 1


values = countdown(10)
for x in values:
    print(x)
    time.sleep(1)


# to generate first n number

def firstN(num):
    n = 1
    while n <= num:
        yield n
        n = n + 1


for x in firstN(10):
    print(x)


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for n in fib():
    if n > 100:
        break
    print(n)
