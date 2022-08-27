def task1(n):
    s = str(n)
    cnt = 0
    for i in s:
        cnt+=int(i)
    return cnt

def task2(n):
    a = [0]*n
    a[1] = 1
    for i in range(1,n):
        a[i] = a[i-1] * i
    return(a)

