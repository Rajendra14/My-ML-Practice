In [ ]:
# A program to implement fibonacci series


def fibonacci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fibonacci(n-1) + fibonacci(n-2)
a=int(input("enter"))
for i in range(1,a+1):
    print(fibonacci(i))
In [ ]:
# MEMOIZATION(a technique to store the value for function call so no repetition to be done in future calls)
# There are two way to implement it

# 1. Implement Explicitly

fibonacci_cache1={}       # created a dict to store the cached values

def fibonacci(n):
    if n in fibonacci_cache1:     #check if it is already present in cache
        return fibonacci_cache1[n]
    else:                        #calculate if not present       
        if n==1:
            return 1
        elif n==2:
            return 1
        elif n>2:
            value= fibonacci(n-1) + fibonacci(n-2)
    
        fibonacci_cache1[n]=value    #storing the value in cache if already not present and then 
        return value                 # return
a=int(input("enter"))
for i in range(1,a+1):
    print(fibonacci(i))
In [ ]:
#Using a builtin Python tool(LRU-LEAST RECENTLY USED CACHE)

from functools import lru_cache
@lru_cache(maxsize=1000)   #If maxsize not given ,by default python takes it to be 128
def fibonacci(n):
    if type(n)!=int:           # check value is of integer type only
        raise TypeError("n must be a positive int")
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fibonacci(n-1) + fibonacci(n-2)
a=int(input("enter"))
if a<1:
        raise ValueError("n must be a positive int")
else:
    for i in range(1,a+1):
        print(fibonacci(i))
