for _ in range(int(input())):
    a = input().split()
    a_num, a_ddakji = int(a[0]), a[1:]

    b = input().split()
    b_num, b_ddakji = int(b[0]), b[1:]

    if a_num < b_num:
        for _ in range(b_num - a_num):
            a_ddakji.append('0')
    else:
        for _ in range(a_num - b_num):
            b_ddakji.append('0')
    
    a_ddakji = ''.join(sorted(a_ddakji)[::-1])
    b_ddakji = ''.join(sorted(b_ddakji)[::-1])

    print('A' if a_ddakji > b_ddakji else ('B' if b_ddakji > a_ddakji else 'D'))