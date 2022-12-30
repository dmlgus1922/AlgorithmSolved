n, k = map(int, input().split())

countries = [list(map(int, input().split())) for _ in range(n)]

countries.sort(key = lambda x: (-x[1], -x[2], -x[3]))

for i in range(n):
    if countries[i][0] == k:
        k_rank = i+1
        break

for i in range(k_rank - 1, -1, -1):
    if i == 0:
        break
    
    if countries[i][1:] == countries[i-1][1:]:
        k_rank -= 1
    else:
        break


print(k_rank)
