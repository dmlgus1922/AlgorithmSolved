n = int(input())

pinary_number = [0, 1]

for _ in range(1, n):
    pinary_number = [pinary_number[0] + pinary_number[1], pinary_number[0]]

print(sum(pinary_number))