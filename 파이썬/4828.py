inputText = open('./sample_input.txt', 'r')
# T = int(input())

for test_case in range(1, T + 1):
    input()
    nums = list(map(int, input().split()))
    print(f'#{test_case} {max(nums) - min(nums)}')