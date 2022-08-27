def task1(a):
    cnt = 0
    for i in range(1,len(a),2):
        cnt+=a[i]
    return cnt

def task2(a):
    l = len(a)//2 + 1 if len(a) % 2 != 0 else len(a)//2
    new_a = [a[i]*a[len(a)-i-1] for i in range(l)]
    return new_a

def task3(a):
    b = [round(i%1,2) for i in a if i%1 != 0]
    return b

def task4(n):
    s =''
    while n != 0:
        s = str(n%2) + s
        n //=2
    return s

def task5(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n+1):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums


#1.   a = [2, 3, 5, 9, 3]
#     print(task1(a))

#2.   a = [2, 3, 4, 5, 6]
#     print(task2(a))

#3.   a = [1.1, 1.2, 3.1, 5, 10.01]
#     b = task3(a)
#     print(max(b) - min(b))

#4.   print(task4(45))

fibo_nums = task5(7)
print(task5(7))
print(fibo_nums.index(0))
