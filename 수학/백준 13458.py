n = int(input())

peoples = list(map(int, input().split()))

supervisor, sub_sup = map(int, input().split())

need = 0

for p in peoples:
    if p < supervisor:
        need += 1
        continue
    p -= supervisor
    need += 1
    div = p // sub_sup
    need += div + 1 if p % sub_sup else div

print(need)
