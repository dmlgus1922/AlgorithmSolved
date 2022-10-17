n, m = map(int, input().split())
num_list = list(map(int, input().split()))
start = 0
end = 0
count = 0
while True:
    if end == len(num_list):
        break
    sum_ = sum(num_list[start:end + 1])
    if sum_ == m:
        count += 1
        start += 1
    elif sum_ < m:
        end += 1
    else:
        start += 1

print(count)