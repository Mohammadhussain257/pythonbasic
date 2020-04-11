from threading import *


def display():
    for i in range(10):
        print('Child thread')
    print('child thread name :', current_thread().getName())


t = Thread(target=display)  # creating of thread object to execute display
t.start()

for i in range(10):
    print('Main Thread')
print('Main thread name : ', current_thread().getName())