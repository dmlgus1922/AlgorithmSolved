def get_leap_year_info(this_year):
    l_year_count = 0
    for i in range(1, this_year):
        if i % 400 == 0:
            l_year_count += 1
        elif i % 100 == 0:
            continue
        elif i % 4 == 0:
            l_year_count += 1

    if this_year % 400 == 0:
        is_leap_year = True
    elif this_year % 100 == 0:
        is_leap_year = False
    elif this_year % 4 == 0:
        is_leap_year = True
    else:
        is_leap_year = False
        
    return l_year_count, is_leap_year


def get_days(y, m, d):
    l_y_cnt, is_l_y = get_leap_year_info(y)

    m_days = [0 for _ in range(m)]

    for i in range(len(m_days)):
        if i == 2 and is_l_y:
            m_days[i] = 29
        elif i == 2 and not is_l_y:
            m_days[i] = 28
        elif i in [1, 3, 5, 7, 8, 10, 12]:
            m_days[i] = 31
        else:
            m_days[i] = 30
            
    
    c_y_cnt = y - l_y_cnt - 1
    days = c_y_cnt * 365 + l_y_cnt * 366 + sum(m_days[1:]) + (d - 1)

    return days


def solution(today, d_day):
    t_y, t_m, t_d = today
    d_y, d_m, d_d = d_day

    if t_y + 1000 < d_y:
        return 'gg'
    elif t_y + 1000 == d_y:
        if t_m < d_m:
            return 'gg'
        elif t_m == d_m and t_d <= d_d:
            return 'gg'
    
    t_days = get_days(t_y, t_m, t_d)
    d_days = get_days(d_y, d_m, d_d)

    return f'D-{d_days - t_days}'
    

if __name__ == '__main__':
    today = list(map(int, input().split()))
    d_day = list(map(int, input().split()))
    
    answer = solution(today, d_day)
    print(answer)
