'''
빨강, 파랑, 노랑이는 시험 문제를 찍기로 했다.
빨강이는 1234512345...로 찍으려 하고 파랑이는 5432154321..., 노랑이는 33333333...으로 찍는다.
시험 문항 수와 답이 주어질 때 가장 많이 맞힌 개수와 사람의 이름을 출력하는 문제이다.
가장 많이 맞힌 사람이 여러명일 경우 빨강, 파랑, 노랑의 순으로 이름을 출력한다.
입력 예)
10
1233512543
출력 예)
7
red

입력 예)
5
21354
출력 예)
1
red
blue
yellow
'''
n = int(input())
answer = input()

blue = []
red = []
yellow = []
blue_ = [str(i) for i in range(5,0,-1)]
red_ = [str(i) for i in range(1,6)]

i = 0
while len(blue) < n:
    if i == 5:
        i = 0
    blue.append(blue_[i])
    red.append(red_[i])
    yellow.append('3')
    i += 1

correct = [0, 0, 0]
people = [red, blue, yellow]

for i in range(n):
    for j in range(3):
        if people[j][i] == answer[i]:
            correct[j] += 1

name = ['red', 'blue', 'yellow']
result = max(correct)

print(result)
while result in correct:
    print(name.pop(correct.index(result)))
    correct.remove(result)
