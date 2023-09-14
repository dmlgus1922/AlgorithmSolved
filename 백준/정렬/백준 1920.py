n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
nums = list(map(int, input().split()))

start = 0
end = n

for num in nums:
    check = []
    while True:   
        mid = (start + end) // 2
        if mid in check:
            print(0)
            start = 0
            end = n
            break
        else:
            check.append(mid)
  
        if num > a[mid]:
            start = mid
        elif num < a[mid]:
            end = mid
        else:
            print(1)
            start = 0
            end = n
            break