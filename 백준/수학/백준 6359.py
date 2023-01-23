t = int(input())

for _ in range(t):
    n = int(input())
    jail = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            if jail[j]:
                jail[j] = 0
            else:
                jail[j] = 1
    print(sum(jail))