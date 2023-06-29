squares = []

max_x = 0
max_y = 0

for _ in range(4):
    square = list(map(int, input().split()))
    squares.append(square)
    max_x = max([max_x, square[0], square[2]])
    max_y = max([max_y, square[1], square[3]])

canvas = [[0 for _ in range(max_x)] for _ in range(max_y)]

for square in squares:
    start_x = square[0]
    end_x = square[2]
    start_y = square[1]
    end_y = square[3]
    for i in range(start_y, end_y):
        for j in range(start_x, end_x):
            canvas[i][j] = 1

print(sum([sum(line) for line in canvas]))