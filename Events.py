'''
Events are something we can trigger and 
when we trigger them some reaction happens.
eg - A button press or some input ..
'''
import time
import threading
event = threading.Event()
def Bomb1():
    print("Bomb is ready waiting for a trigger...")
    if event.wait(): # Thread waits for a signal. 
        print("Bomb1 Exploded !")

def Bomb2():
    print("Bomb is ready waiting for a trigger...")
    if event.wait():
        print("Bomb2 Exploded !")

def Bomb3():
    print("Bomb is ready waiting for a trigger...")
    if event.wait(): 
        print("Bomb3 Exploded !")

def Trigger():
    input("Enter to explode >> ")
    event.set() 

Bomb1Thred = threading.Thread(target = Bomb1)
Bomb2Thred = threading.Thread(target = Bomb2)
Bomb3Thred = threading.Thread(target = Bomb3)
TriggerThread = threading.Thread(target = Trigger)

Bomb1Thred.start()
Bomb2Thred.start()
Bomb3Thred.start()
TriggerThread.start()