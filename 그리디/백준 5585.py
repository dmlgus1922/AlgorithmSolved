change = 1000 - int(input())

coins = [500, 100, 50, 10, 5, 1]

count = 0

for coin in coins:
    coin_num = change // coin
    count += coin_num
    change -= coin_num * coin

print(count)