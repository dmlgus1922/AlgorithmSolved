n = int(input())

fac = 1

for i in range(1, n+1):
    fac *= i

count = 0

for num in str(fac)[::-1]:
    if num == '0':
        count += 1
    else:
        print(count)
        break