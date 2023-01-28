nums = [list(map(int, input().split())) for _ in range(9)]

max_num = 0
col = 0
row = 0

for i in range(9):
    for j in range(9):
        if nums[i][j] > max_num:
            max_num = nums[i][j]
            col = i
            row = j

print(max_num, f'{col + 1} {row + 1}', sep = '\n')