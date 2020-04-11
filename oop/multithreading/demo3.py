import time
from threading import *


# without threading more time it required for execution
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print('Double Value : ', 2 * n)


def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print('Square Value : ', n * n)


numbers = [1, 2, 3, 4, 5, 6]
begintime = time.time()
doubles(numbers)
squares(numbers)
endtime = time.time()
print('Total time taken : ', endtime - begintime)


# with threading

def double(number):
    for n in number:
        time.sleep(1)
        print('Double value : ', 2 * n)


def square(number):
    for n in number:
        time.sleep(1)
        print('Square Value : ', n * n)


number = [1, 2, 3, 4, 5, 6]
startTime = time.time()
t1 = Thread(target=double, args=(number,))
t2 = Thread(target=square, args=(number,))
t1.start()
t2.start()
t1.join()
t2.join()
endTime = time.time()
print('Total time taken : ', startTime - endTime)
