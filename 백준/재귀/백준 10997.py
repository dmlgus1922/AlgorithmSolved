def star(n):
    if n == 1:
        return ['*']
    if n == 2:
        return ['*****', '*', '* ***', '* * *', '* * *', '*   *', '*****']

    pre_star = star(n - 1)
    stars_height = 4 * n - 1
    stars_width = 4 * n - 3
    stars = ['' for _ in range(stars_height)]

    for i in range(len(pre_star)):
        stars[i + 2] += '* ' + pre_star[i]
        if i == 0:
            stars[i + 2] += '**'
        elif i == 1:
            stars[i + 2] += ' ' * (4 * n - 7) + '*'
        else:
            stars[i + 2] += ' *'

    stars[0] += '*' * stars_width
    stars[1] += '*'
    stars[-2] += '*' + ' ' * (stars_width - 2) + '*'
    stars[-1] += '*' * stars_width

    return stars

print(*star(int(input())), sep = '\n')