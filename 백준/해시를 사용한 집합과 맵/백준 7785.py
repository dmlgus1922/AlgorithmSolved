company = {}

n = int(input())

for _ in range(n):
    name, state = input().split()
    company[name] = state

answer = [name for name, state in company.items() if state == 'enter']

print(*sorted(answer, reverse=True), sep = '\n')