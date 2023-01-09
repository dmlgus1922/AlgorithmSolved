'''
재귀 사용

예제는 다 맞지만 시간초과 걸림
반복문으로 다시 풀 예정

n = int(input())
p = list(map(int, input().split()))
p.insert(0,0)

def getMoney(n):
    if n == 0:
        return p[0]
    if n == 1:
        return p[1]
    
    max_ = p[n]
    
    for i in range(n, 0, -1):
        max_ = max(max_, p[i] + getMoney(n-i))
    
    return max_
      
print(getMoney(n))
'''