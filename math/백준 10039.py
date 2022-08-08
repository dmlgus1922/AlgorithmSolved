sum_ = 0
for _ in range(5):
    x = int(input())
    if x < 40:
        x = 40 // 5
    else:
        x //= 5
    sum_ += x
print(sum_)