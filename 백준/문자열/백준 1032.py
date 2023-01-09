n = int(input())
s_l = [input() for _ in range(n)]
answer = ''
for i in range(len(s_l[0])):
    check = s_l[0][i]
    for s in s_l:
        if check != s[i]:
            answer += '?'
            break
    else:
        answer += check
print(answer)