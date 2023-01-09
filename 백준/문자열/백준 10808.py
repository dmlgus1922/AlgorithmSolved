alpha = dict(zip(list('abcdefghijklmnopqrstuvwxyz'), [0 for _ in range(26)]))

for s in input():
    alpha[s] += 1

print(*alpha.values())
