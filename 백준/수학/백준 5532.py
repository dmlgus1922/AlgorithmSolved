l, a, b, c, d = [int(input()) for _ in range(5)]

while a > 0 or b > 0:
    l -= 1
    a -= c
    b -= d

print(l)