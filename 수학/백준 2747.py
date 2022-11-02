fibo = [0 for _ in range(int(input()) + 1)]

for i in range(len(fibo)):
    if i == 0:
        continue
    elif i == 1:
        fibo[i] = 1
    else:
        fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[-1])

'''
재귀용법

def fibo(n) :
    if n == 0 :
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(int(input())))
'''