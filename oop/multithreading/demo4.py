from threading import *
import time


def display():
    print(current_thread().name, '...started')
    time.sleep(2)
    print(current_thread().name, '...ended')


print('Number of active thread : ', active_count())
t1 = Thread(target=display, name='ChildThread-1')
t2 = Thread(target=display, name='ChildThread-2')
t3 = Thread(target=display, name='ChildThread-3')
t1.start()
t2.start()
t3.start()
print('Number of active thread : ', active_count())
time.sleep(3)
print('Number of active thread : ', active_count())
