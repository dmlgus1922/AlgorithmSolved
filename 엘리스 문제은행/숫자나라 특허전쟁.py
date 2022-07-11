'''
숫자나라에서 3과 5의 배수에 특허를 내 그 수들을 맘대로 사용할 수 없게 되었다.
입력받는 수(n) 미만의 자연수들 중 사용할 수 없는 수들의 합을 구하는 프로그램.

입력 예)
자연수 n을 입력한다 (1 <= n <= 100000) 
출력 예)
23
'''
n = [i for i in range(1, int(input()))]
n.insert(0,0)
sum_ = sum(n)
for i in range(0,len(n),3):
    n[i] = 0
for i in range(0, len(n), 5):
    n[i] = 0
print(sum_ - sum(n))