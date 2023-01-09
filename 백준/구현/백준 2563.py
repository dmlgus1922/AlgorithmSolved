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
# x = []
# y = []
# n = int(input())
# total = n * 100
# for _ in range(n):
#     x1, y1 = map(int, input().split())
#     x.append(x1)
#     y.append(y1)

# minus = 0
# for i in range(n):
#     for j in range(i+1, n):
#         big_x = max(x[i], x[j])
#         small_x = min(x[i], x[j])
#         big_y = max(y[i], y[j])
#         small_y = min(y[i], y[j])
#         if big_x - small_x < 10 or big_y - small_y < 10:
#             width = small_x + 10 - big_x
#             height = small_y + 10 - big_y
#             minus += width * height

# print(total - minus)
# 겹치는 부분이 중복으로 빠져서 틀린다. 


# 2차원 배열로 도화지를 그리고 색칠된 부분을 1로 초기화하면 쉽게 구할 수 있다.
n = int(input())
x_list = []
y_list = []
for _ in range(n):
    x, y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)

width = max(x_list) +10
height = max(y_list) +10
paper = [[0 for _ in range(width)] for _ in range(height)]

for i in range(n):
    x = x_list[i]
    y = y_list[i]
    for y_index in range(y, y+10):
        for x_index in range(x, x+10):
            paper[y_index][x_index] = 1

result = sum([sum(p) for p in paper])
# print(*paper, sep = '\n')
print(result)