n, kim, lim = map(int, input().split())

players = list(range(n))
kim -= 1
lim -= 1

kimIdx = players.index(kim)
limIdx = players.index(lim)

round_ = 1
while True:
    if (kimIdx % 2 == 0 and limIdx == kimIdx+1) or (limIdx % 2 == 0 and kimIdx == limIdx+1):
        break
    kimIdx = kimIdx//2
    limIdx = limIdx//2
    round_ += 1

print(round_)
