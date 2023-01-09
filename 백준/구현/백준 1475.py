room = list(input())
count_ = []
for i in range(len(room)):
    if room[i] == '6':
        room[i] = '9'
for s in room:
    if s == '9':
        count_.append((room.count(s)+1)//2)
    else:
        count_.append(room.count(s))

print(max(count_))