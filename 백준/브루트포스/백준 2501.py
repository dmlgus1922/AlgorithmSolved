n, k = map(int, input().split())

yaksoo = [i for i in range(1, n+1) if n % i == 0]

print(yaksoo[k - 1] if len(yaksoo) >= k else 0)