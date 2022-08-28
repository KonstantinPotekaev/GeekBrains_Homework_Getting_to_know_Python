import math

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

#print(task1(100))
print(*task2([1,1,2,3,4,4,5]))
