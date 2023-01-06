A_B = [1, 0]

for i in range(int(input())):
    A_B = [A_B[1], A_B[0] + A_B[1]]

print(*A_B)