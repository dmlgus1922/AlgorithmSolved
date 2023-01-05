n = int(input())

mountains = list(map(int, input().split()))

start = mountains[0]
temp_best = 0
best = 0

for m in mountains:
    if m > start:
        start = m
        best = max(best, temp_best)
        temp_best = 0
        continue
    if m < start:
        temp_best += 1
else:
    best = max(best, temp_best)

print(best)