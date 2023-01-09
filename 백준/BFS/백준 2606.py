from collections import deque
com_num = int(input())
line = int(input())
com_connect = [[] for _ in range(com_num+1)]

for _ in range(line):
    com1, com2 = map(int, input().split())
    com_connect[com1].append(com2)
    com_connect[com2].append(com1)

virus = [1]
visited = deque([1])
order = [1]

while visited:
    for com in order:
        for c in com_connect[com]:
            if c not in virus:
                virus.append(c)
                visited.append(c)
        visited.popleft()
    order = list(visited)

print(len(virus)-1)