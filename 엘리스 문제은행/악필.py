'''
보영이는 글자를 흘려 쓰는 버릇이 있습니다. 
특히 그녀가 적은 숫자를 보았을 때, ‘7’이 ‘9’처럼 보일 때도 있고, 
‘9’가 ‘7’처럼 보일 때가 있습니다.
보영이가 숫자 A와 B를 적었다고 합니다. 
이 두 개의 수를 본 뒤, 더한다고 할 때 
존재할 수 있는 값의 최댓값과 최솟값을 출력하는 프로그램을 작성하세요.

입력
첫 번째 줄에 보영이가 적은 두 개의 수 A, B를 입력합니다.
(1 ≤ A, B ≤ 1,000,000)
출력
첫 번째 줄에 두수의 합의 최댓값과 최솟값을 출력합니다.

입력 예)
7912 1270

출력 예)
11202 8982
'''

def nine(x):
    for num in x:
        if num == '7':
            x = '9'.join(x.split('7'))
    return int(x)

def seven(x):
    for num in x:
        if num == '9':
            x = '7'.join(x.split('9'))
    return int(x)

a, b = input().split()

print(nine(a)+nine(b),seven(a)+seven(b))