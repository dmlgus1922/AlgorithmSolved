while True:
    string = input()
    if string == '#':
        break
    answer = 0
    for s in string:
        if s in 'aeiouAEIOU':
            answer += 1
    print(answer)