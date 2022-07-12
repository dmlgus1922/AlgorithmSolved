'''
도도새는 10이하의 길이를 가진 문자열이 적힌 반지를 n개 가지고 있다.
도도새는 반지에 적힌 문자열을 시계방향으로 읽는다.
그러나 모자장수의 닉네임이 적혀있다면 이는 도도새의 반지가 아닌 모자장수의 반지이다.
입력의 첫 번째 줄에 모자장수의 닉네임, 두 번째 줄에 반지의 수(n),
그 다음 줄부터 각 반지에 적힌 문자열이 주어질 때 모자장수의 반지의 수를 출력하는 문제이다.

입력 예)
ABC
2
ABCAAAAAAA
CWEQWFGAB
출력 예)
2
'''
nickmname = input()
n = int(input())
rings = [input()*2 for _ in range(n)]
hat = 0
for ring in rings:
    if nickmname in ring:
        hat += 1
print(hat)