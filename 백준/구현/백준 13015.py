def stars(n):
    length = 2 * n - 1
    star = ['' for _ in range(length)]

    for i in range(n - 1):
        if i == 0:
            star[i] = f"{'*' * n}{' ' * (length - 2)}{'*' * n}"
        else:
            star[i] = f"{' '*i}*{' ' * (n - 2)}*{' ' * (length - 2 * (i + 1))}*{' ' * (n - 2)}*"

        star[length - 1 - i] = star[i]

    star[n-1] = f"{' '*(n-1)}*{' '*(n - 2)}*{' '*(n - 2)}*"

    return star

print(*stars(int(input())), sep = '\n')