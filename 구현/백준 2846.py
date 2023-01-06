n = int(input())

road = list(map(int, input().split()))

start = road[0]
temp = 0
height = 0

for r in road:
    if r > temp:
        temp = r
        continue
    else:            
        height = max(height, temp - start)
        start = r
        temp = r
else:
    height = max(height, temp - start)

print(height)