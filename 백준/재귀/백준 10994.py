star1_num = 4 * 1 - 3

star1 = ['' for _ in range(star1_num)]

star1[0] += '*' * star1_num

print(*star1)
print()


star2_num = 4 * 2 - 3
star2 = ['' for _ in range(star2_num)]

star2[0] += '*' * star2_num
star2[1] += '*' + ' ' * (star2_num - 2) + '*'
star2[2] += '*' + star1[0] + '*'
star2[3] += '*' + ' ' * (star2_num - 2) + '*'
star2[4] += '*' * star2_num

print(*star2, sep = '\n')


def stars(n):
    if n == 1:
        return ['*']
    
    pre_star = stars(n-1)
    star_num = 4 * n - 3
    star = ['' for _ in range(star_num)]
    
    star[0] += 
        
    


'''
1 - 1

2 - 5

3 - 9

4 - 13
23.02.08 푸는 중
'''
