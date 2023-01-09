n = int(input())

ans = [0 for _ in range(n+1)]

try:
    ans[1]=0
    ans[2]=1
    ans[3]=1
    for i in range(4, n + 1):
        if i % 2 == 0 and i % 3 == 0:
            temp = min(ans[i-1], ans[i//2], ans[i//3])
        elif i % 2 == 0:
            temp = min(ans[i//2], ans[i-1])
        elif i % 3 == 0:
            temp = min(ans[i//3], ans[i-1])
        else:
            temp = ans[i-1]
        ans[i] = temp + 1
    print(ans[n])

except:
    if n == 1:
        print(0)
    else:
        print(1)
