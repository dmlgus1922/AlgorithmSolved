'''
n개의 훌라후프가 붙어있다. 
첫 번째 훌라후프가 한 바퀴 돌아갈 때 나머지 n-1개의 훌라후프가 얼마만큼 돌아가는지 구하는 문제이다.
첫째 줄에 훌라후프 개수(n)가 주어지고 다음 줄에 그 수에 맞은 훌라후프 반지름이 주어진다.
출력은 n-1개의 줄로 기약분수 형태 A/B로 훌라후프가 몇 바퀴 도는지 출력한다.

입력 예)
4
12 3 8 4

출력 예)
4/1
3/2
3/1

유클리드 호제법을 이용했다. 이제 충분히 익혀서 쉽게 풀 수 있었다.
'''

n = int(input())
hoop = list(map(int, input().split()))
def G(x, y):
    while True:
        if x % y == 0:
            return y
        x, y = y, x % y

for i in range(1,n):
    g = G(hoop[0], hoop[i])
    print(f'{hoop[0]//g}/{hoop[i]//g}')