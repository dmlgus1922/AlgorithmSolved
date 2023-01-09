people = 0
people_max = 0

for _ in range(4):
    off, on = map(int, input().split())
    people = people - off + on
    people_max = max(people_max, people)

print(people_max)