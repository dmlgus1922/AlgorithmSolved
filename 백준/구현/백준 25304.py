x = int(input())
n = int(input())
sum_ = 0
for _ in range(n):
    price, num = map(int,input().split())
    sum_ += price * num

if sum_ == x:
    print('Yes')
else:
    print('No')