string = input()

tag = False
stack  = []
answer = ''

for s in string:
    if s == '<':
        tag = True
    elif s == '>':
        answer += s
        tag = False
        continue

    while stack and (s == ' ' or tag):
        answer += stack.pop()
    
    if tag or s == ' ':   
        answer += s
    else:
        stack.append(s)

while stack:
    answer += stack.pop()
    
print(answer)