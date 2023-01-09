n, m = map(int, input().split())
answer = []

for i in range(2):
    if i == 0:
        for _ in range(n):
            answer.append(list(map(int, input().split())))
    else:
        for j in range(n):
            plus = list(map(int, input().split()))
            for k in range(m):
                answer[j][k] += plus[k]
            print(*answer[j])