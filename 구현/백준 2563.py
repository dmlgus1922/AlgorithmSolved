'''
100 * n에서 겹치는 부분만 빼면 된다.
3 5 15
7 2 7

3 13, 5 15, 15 25
7 17, 2 12, 7 17

3 13, 7 17
5 15, 2 12
15 25, 7 17

3
3 7
15 7
5 2
'''
x = []
y = []
n = int(input())
total = n * 100
for _ in range(n):
    x1, y1 = map(int, input().split())
    x.append(x1)
    y.append(y1)

minus = 0
for i in range(n):
    for j in range(i+1, n):
        big_x = max(x[i], x[j])
        small_x = min(x[i], x[j])
        big_y = max(y[i], y[j])
        small_y = min(y[i], y[j])
        if big_x - small_x < 10 or big_y - small_y < 10:
            width = small_x + 10 - big_x
            height = small_y + 10 - big_y
            minus += width * height

print(total - minus)