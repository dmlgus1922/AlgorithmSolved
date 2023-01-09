input()
arr = []
for _ in range(2):
    temp_arr = list(map(int, input().split()))
    arr.extend(temp_arr)
print(*sorted(arr))