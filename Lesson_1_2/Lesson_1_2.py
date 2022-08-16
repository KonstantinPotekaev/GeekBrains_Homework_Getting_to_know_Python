import math
from xmlrpc.client import boolean
import numpy as np

def task1(a, b):
    return math.sqrt(max(a,b)) == min(a,b)

def task2(a):
    return max(a) # a Ч массив чисел

def task3(n):
    a = np.arange(-n,n+1)
    return a

def task4(n):
    return (int(n*10)%10)

def task5(n):
    return ((not n%10 and not n%5) or (not n%15 and boolean(n%30)))

def task6(n):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return (days[n-1], n-1 == 5 or n-1 == 6)

#print(*task3(10000))
#print(task4(10.9138))
#print(task5(45))
print(*task6(3))

