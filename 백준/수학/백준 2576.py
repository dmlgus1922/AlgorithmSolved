ans = []
for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        ans.append(n)
if not ans: print(-1)
else: print(sum(ans), min(ans), sep = '\n')