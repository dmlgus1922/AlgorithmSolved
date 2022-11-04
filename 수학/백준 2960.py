n, k = map(int, input().split())

nums = [0 for _ in range(n + 1)]

check = 0

for i in range(2, n+1):
    if not nums[i]:
        for j in range(i, n+1, i):
            if not nums[j]:
                nums[j] = 1
                check += 1
            
            if check == k:
                print(j)
                break