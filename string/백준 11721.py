st = input()
for idx, s in enumerate(st):
    print(s, end='')
    if (idx+1) % 10 == 0:
        print()