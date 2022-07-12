'''
도도새는 어떤 물건을 넣고 돌리면 같은 물건이 무한으로 반복해 나오는 맷돌을 얻었다.
도도새는 이 맷돌에 문자열을 넣고 돌리려 한다.
두 문자열 s와 t가 주어졌을 때 두 문자열을 맷돌에 넣고 같은 문자열을 만들 수 있으면 1
아니면 0을 출력하는 문제이다.

입력 예)
abc
abcabc
출력 예)
1

s와 t의 길이가 50보다 작거나 같은 자연수라 for문으로 1부터 50까지 돌며 한 문자열을 곱해줬다.
그 결과가 다른 문자열과 같다면 1을 출력하는 함수를 만들었는데 'aa', 'aaa'와 같은 반례가 있었다.
이를 해결하기 위해 유클리드 호제법을 이용, 상대방의 문자열 길이를 최대공약수로 나눈 값으로 자기 자신 문자열을 곱한다면
둘은 같은 문자열이 된다. 이를 이용한 문제풀이.
'''
s = input()
t = input()

def u(s,t):
    x = len(s)
    y = len(t)
    while x % y != 0:
        x,y = y, x % y
    return len(t) // y, len(s) // y


def check(s,t):
    x, y = u(s,t)
    if s*x == t*y:
        return 1
    for i in range(51):
        if s * i == t:
            return 1
    else:
        return 0

if check(s,t) == 1 or check(t,s) == 1:
    print(1)
else:
    print(0)