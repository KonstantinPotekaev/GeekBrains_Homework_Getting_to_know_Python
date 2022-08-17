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

def logical_statement1(x, y, z):
    return (not (x or y or z)) == (not x and not y and not z)
def logical_statement():
    return (logical_statement1(0, 0, 0) and logical_statement1(0, 0, 1) and logical_statement1(0, 1, 0) and logical_statement1(0, 1, 1) and logical_statement1(1, 0, 0) and logical_statement1(1, 0, 1) and logical_statement1(1, 1, 0) and logical_statement1(1, 1, 1))

def task8(x,y):
    if x == 0 and y == 0:
        return('At the point 0,0...')
    elif x == 0:
        print('Abscissa axis')
    elif y == 0:
        return('Ordinate axis')
    if x>0 and y>0:
        return('I')
    elif x<0 and y>0: 
        return('II') 
    elif x<0 and y<0: 
        return('III') 
    elif x>0 and y<0: 
        return('IV') 

def task10(x1,y1,x2,y2):
    return (math.sqrt((x2-x1)**2 + (y2-y1)**2))
#print(*task3(10000))
#print(task4(10.9138))
#print(task5(45))
#print(*task6(3))
#print(logical_statement())
#print(task8(1,2))
print(task10(10,34,3,10))


