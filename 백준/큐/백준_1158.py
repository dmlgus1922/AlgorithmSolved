from collections import deque
n, k = map(int, input().split())
n_deque = deque([str(i) for i in range(1, n+1)])

josephus = []

while n_deque:
    for _ in range(k-1):
        n_deque.append(n_deque.popleft())
    josephus.append(n_deque.popleft())

josephus = ', '.join(josephus)
print('<' + josephus + '>')