'''
계속 절반으로 자르는데 시작하는 숫자가 64.
2의 n제곱수들로만 나온다.
결국 주어진 숫자를 2진수로 바꿔 1이 몇 개인지만 찾으면 됨.
'''

def bin(n, b):
    if n == 1:
        b.append(1)
        return

    else:
        b.append(n%2)
        return bin(n//2,b)

b = []
n = int(input())
bin(n, b)

print(sum(b))