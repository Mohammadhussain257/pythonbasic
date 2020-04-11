# the thread that may run in the background or background executing thread
# the main purpose of daemon thread is to provide support for non-daemon thread (main thread)
# eg of daemon thread is garbage collection which always running in the background

from threading import *

mt = current_thread()
print(current_thread().getName())
print('Is main thread is a daemon thread : ', mt.isDaemon())