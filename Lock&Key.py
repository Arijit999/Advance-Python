import threading
import time

'''
If lock is there then it will create 
a deadlock condition as one thread increases 
a value and other tryes to decrease.
''' 
# Uncomment to enable lock
shared_resource = 5
lock = threading.Lock()
def DecreaseNumber():
    global shared_resource
    #lock.acquire()
    while(shared_resource>0):
        shared_resource -= 1
        time.sleep(1)
        print(shared_resource)  
    print("Lowest Value reached")
    #lock.release()

def IncreaseNumber():
    global shared_resource
    #lock.acquire()
    while(shared_resource<10):
        shared_resource += 1
        time.sleep(1)
        print(shared_resource)  
    print("Lowest Value reached")
    #lock.release()

t1 = threading.Thread(target= DecreaseNumber)
t2 = threading.Thread(target= IncreaseNumber)

t1.start()
t2.start()