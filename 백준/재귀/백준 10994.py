def stars(n):
    if n == 1:
        return ['*']
    
    pre_star = stars(n-1)
    pre_star_num = 4 * (n - 1) - 3

    star_num = 4 * n - 3
    star = ['' for _ in range(star_num)]
    
    star[0] += '*' * star_num
    star[1] += '*' + ' ' * (star_num - 2) + '*'
    star[-2] += '*' + ' ' * (star_num - 2) + '*'
    star[-1] += '*' * star_num

    for i in range(pre_star_num):
        star[i + 2] += '* ' + pre_star[i] + ' *'

    return star

print(*stars(int(input())), sep = '\n')