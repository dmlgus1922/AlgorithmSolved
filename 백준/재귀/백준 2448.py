n = int(input())

def stars(n):
    if n == 3:
        return ['  *', ' * *', '*****']

    star_n = ['' for _ in range(n)]
    pre_n = n // 2
    pre_star = stars(pre_n)
    
    for i in range(n):
        if i < pre_n:
            star_n[i] += ' ' * (pre_n)
            star_n[i] += pre_star[i % pre_n]
        else:
            star_n[i] += pre_star[i % pre_n]
            star_n[i] += ' ' * (pre_n - i % pre_n)
            star_n[i] += pre_star[i % pre_n]
    return star_n

answer = stars(n)

for i in range(n):
    answer[i] += ' ' * (n - i - 1)

print(*answer, sep = '\n')