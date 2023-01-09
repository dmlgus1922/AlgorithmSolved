import string

low = list(string.ascii_lowercase * 2)
up = list(string.ascii_uppercase * 2)

answer = ''

for s in input():
    if s.isupper():
        answer += up[up.index(s) + 13]
    elif s.islower():
        answer += low[low.index(s) + 13]
    else:
        answer += s
print(answer)
