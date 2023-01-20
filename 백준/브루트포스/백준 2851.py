next_score = 0

for _ in range(10):
    pre_score = next_score
    next_score += int(input())

    pre_diff = abs(100 - pre_score)
    next_diff = abs(100 - next_score)

    if pre_diff < next_diff:
        print(pre_score)
        break
    
else:
    print(next_score)
