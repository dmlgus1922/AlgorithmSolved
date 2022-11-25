price, n, money = map(int, input().split())

parent_money = price * n - money

print(parent_money if parent_money >= 0 else 0)
