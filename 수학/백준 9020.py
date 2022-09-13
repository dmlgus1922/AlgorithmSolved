p_list = list(range(10001)) # 0부터 10000까지의 수를 리스트에 저장
p_list[0], p_list[1] = 0, 0 # 0과 1은 처음부터 제외를 한다.

# 10000까지의 수 중 소수(prime number)만 골라내는 작업을 한다.
# 에라토스테네스의 체를 이용.
for p in p_list:
    if p != 0:
        for j in range(p*2, 10001, p):  # p의 배수는 모두 지워지게 되는 것.
            p_list[j] = 0

# 중복 제거, 정렬, 0제거 후엔 소수만 남은 리스트가 된다.
p_list = set(p_list)
p_list = sorted(list(p_list))
p_list.remove(0)


t = int(input())
for _ in range(t):
    n = int(input())
    ans = []
    for p in p_list:   
        if p > n-p:   # p가 n-p보다 큰 경우는 이미 앞에서 고려를 한 경우이다. 그 후의 p들도 마찬가지이므로 for문을 탈출하며 시간을 절약한다.
            break
        elif n-p in p_list:  #n-p도 소수이면 정답 리스트에 추가한다.
            ans.append(p)
            ans.append(n-p)
    print(ans[-2], ans[-1]) # 가장 마지막에 추가한 두 소수가 차이가 가장 적은 두 소수.
