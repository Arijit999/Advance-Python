''' 
Semaphores limit the access of a shared resource / critical section
it only allows 'n' number of threads to access a shared resource
but not  unlimited.
'''
import threading
import time

semaphore = threading.BoundedSemaphore(5) # Only grants 5 threads at once
def access(Thread_number):
    print(f"{Thread_number} trying to access")
    semaphore.acquire()
    print(f"{Thread_number} was granted access")
    time.sleep(10)
    print(f"{Thread_number} is releasing")
    semaphore.release()

for thread_number in range(1,11):
    t = threading.Thread(target=access,args=(thread_number,))
    t.start()
    time.sleep(1)
    