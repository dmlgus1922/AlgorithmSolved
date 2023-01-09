n = int(input())

is_cute = [int(input()) for _ in range(n)]

print('Junhee is cute!' if sum(is_cute) > n // 2 else 'Junhee is not cute!')