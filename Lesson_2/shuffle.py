import random

def shuffle1(a):
    n = len(a)
    for i in range(n-1,0,-1):
        j = random.randint(0,i)
        a[i],a[j] = a[j],a[i]
    return a

    




