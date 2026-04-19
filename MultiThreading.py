'''
Thread - A small part of a process, light weight as 
it shares the same resources allocated to the the process. 
It can executes different parts of a program concurrently

Threads simulate parallelism by switching threads frequently
but not true parallelisn (Bounded by GIL)
GIL only releases a thread during I/O.

time.sleep() - Releases the GIL as .sleep() is treated as I/O operation.
( .sleep() Not = True Parallelism)
'''

import threading 
import time

def fun1 ():
    for i in range(4):
        time.sleep(1) 
        print("Function 1")

def fun2 ():
    for i in range(8):
        time.sleep(1)
        print("Function 2")

t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)

'''
.run() does not start a new thread at all. 
It just executes the function in the current
thread, like a normal function call.
'''
t1.run()
t2.run()

t1.start() # .start() runs the thread in parallel
t2.start()

'''
Usually the unthreated part of a program also runs 
parallely but, If you want to explecitely run rest 
of the program after a thread completes use .join() 
'''

t1.join()
print("Run after a thread 1 completes")

