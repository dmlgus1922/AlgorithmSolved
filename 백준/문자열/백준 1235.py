n = int(input())
st_num = []

for _ in range(n):
    st_num.append(input()[::-1])


for i in range(1, len(st_num[0]) + 1):
    new_num = set()
    for num in st_num:
        new_num.add(num[:i])

    if len(new_num) == n:
        print(i)
        break