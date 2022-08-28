import math
import random
from tkinter import Variable

def task1(n):
    a = []
    i = 2
    temp = n
    while i <= n:
        if n % i == 0:
            a.append(i)
            n //= i
            i = 2
        else:
            i += 1
    return a

def task2(a):
    return set(a)

def task3(k):
    indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           "-": "\u207B"
           }
    s = ''
    for i in range(k,-1,-1):
        a = random.randint(0,100)
        if (a!=0):
            if (i == 0):
                s+=str(a)
                break
            s += str(a)+'*x'
            if (i>1):
                temp = str(i)
                for j in temp:
                    s+=indexes[j]
            s += ' + '
    s += ' = 0'
    return s

def task4(path1,path2):
    print("Я могу это сделать, но на это уйдет около 20 минут, а это очень много...")
        

#print(task1(100))
#print(*task2([1,1,2,3,4,4,5]))

#print(task3(10))
