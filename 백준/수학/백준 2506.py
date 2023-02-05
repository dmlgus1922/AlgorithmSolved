n = int(input())
score = input().replace(' ', '').split('0')
sum_score = 0
for s in score:
    for i in range(1, len(s) + 1):
        sum_score += i

print(sum_score)