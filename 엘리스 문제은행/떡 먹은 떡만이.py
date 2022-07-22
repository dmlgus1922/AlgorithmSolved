'''
세 쌍둥이 떡만이 1, 2, 3이 일렬로 서 있다.
그 중 떡만이1이 떡을 먹어버렸다.
셋 중 두 명이 자리를 서로 m번 바꿀 때 떡을 먹은 떡만이 1을 찾는 문제이다.

입력 첫 줄에 자리를 바꿀 횟수 m,
다음 m번의 줄에 두 자리 번호가 공백을 기준으로 주어진다.
입력 예)
4
3 1
2 3
3 1
3 2

떡을 먹은 떡만이1의 자리를 출력한다.
출력 예)
3
'''
m = int(input())
dm = {1:1, 2:2, 3:3}
for _ in range(m):
    x,y = map(int, input().split())
    first = dm[x]
    second = dm[y]
    dm[x] = second
    dm[y] = first
item = list(dm.items())
item.sort(key = lambda x: x[1])
print(item[0][0])
