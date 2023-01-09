n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort(reverse = True)

max_weight = 0
for i in range(1,n+1):
    max_weight = max(rope[i-1] * i, max_weight)
print(max_weight)