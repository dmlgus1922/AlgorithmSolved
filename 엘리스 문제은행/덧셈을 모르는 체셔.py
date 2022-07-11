'''
학교에서 덧셈을 배운 체셔가 동생에게 덧셈 알려주려고 한다.
그러나 덧셈 기호를 쓰는 방법을 잊어버려서 공백 없이 숫자만 두 개 나열하는데 이의 합을 구하는 문제이다.
주어지는 숫자는 1이상 10이하이다.
입력 예)
102
출력 예)
12

입력 예)
37
출력 예)
10
'''
plus = input()
if len(plus) == 4:
    a = plus[:2]
    b = plus[2:]
else:
    if plus[1] =='0':
        a = plus[:2]
        b = plus[2]
    else:
        a = plus[0]
        b = plus[1:]
    
a, b = map(int, (a,b))
print(a+b)