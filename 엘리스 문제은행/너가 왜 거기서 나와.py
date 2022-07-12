'''
엘리스 토끼와 도도새는 1부터 n까지의 수를 이어서 새로운 하나의 수를 얻었다.
(1234567891011121314...)
그런데 엘리스는 n이라는 숫자를 직접 쓰지 않더라도 이어서 쓴 숫재 네에서 찾을 수 있다는 걸 알아냈다.
예를들어 n=121일 때 14번째 숫자에 121이 있었다.
ex) 1234567891011(121)3
n이 주어졌을 때 n이 가장 먼저 등장하는 위치를 알아내는 문제이다.

입력 예)
121
출력 예)
14
'''
n = int(input())
def answer(n):
    check_n = str(n)
    num_str = ''
    for i in range(1,n+1):
        i = str(i)
        num_str += i
    if check_n in num_str:
        return num_str.find(check_n)
print(answer(n)+1)