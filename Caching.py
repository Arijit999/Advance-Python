from  functools import lru_cache
import time

@lru_cache(maxsize=None)
def fun(n):
    time.sleep(2)
    return "Number : "+str(n)

# Take some time to execute
print("Before caching")
Start=time.time()
print(fun(2))
print(fun(5))
print(fun(7))
End=time.time()
print("Total time before caching :",End-Start) # More or less 6 sec 

# Takes almost negligible time to execute because of caching
print("\nAfter caching")
Start=time.time()
print(fun(2))
print(fun(5))
print(fun(7))
End=time.time()
print("Total time after caching :",End-Start) # 0 sec


