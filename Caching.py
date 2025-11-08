from  functools import lru_cache
import time

@lru_cache(maxsize=None)
def fun(n):
    time.sleep(2)
    return "Number : "+str(n)

print("Before caching")
Start=time.time()
print(fun(2))
print(fun(5))
print(fun(7))
End=time.time()
print("Total time before caching :",End-Start)

print("\nAfter caching")
Start=time.time()
print(fun(2))
print(fun(5))
print(fun(7))
End=time.time()
print("Total time after caching :",End-Start)

