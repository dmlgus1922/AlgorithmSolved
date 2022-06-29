e, s, m = map(int, input().split())

year = 1
e1 = s1 = m1 = 1

while (e1,s1,m1) != (e, s, m):
    e1 += 1
    s1 += 1
    m1 += 1
    if e1 >= 16:
        e1 = 1
    if s1 >= 29:
        s1 = 1
    if m1 >= 20:
        m1 = 1

    year += 1

print(year)
