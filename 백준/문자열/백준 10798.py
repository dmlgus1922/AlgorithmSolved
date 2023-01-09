string = []
max_len = 0
for _ in range(5):
    temp_s = input()
    string.append(temp_s)
    max_len = max(len(temp_s), max_len)

for i in range(5):
    temp = max_len - len(string[i])
    string[i] += ' ' * temp

for i in range(max_len):
    for j in range(5):
        if string[j][i] != ' ':
            print(string[j][i], end = '')