n = int(input())

def star(n):
    if n == 3:
        return ['***', '* *', '***']
    star_list = ['' for _ in range(n)]
    pre_n = n // 3
    pre_star = star(pre_n)
    for i in range(3):
        for j in range(n):
            if i == 1 and pre_n <= j < pre_n * 2:
                star_list[j] += ' ' * pre_n
                continue
            star_list[j] += pre_star[j % pre_n]
    return star_list

print(*star(n), sep = '\n')