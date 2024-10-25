def solution(video_len, pos, op_start, op_end, commands):
    def time_value(t):
        m, s = map(int, t.split(':'))
        return m * 60 + s
    
    def time_format(n):
        if n < 10:
            return f'0{n}'
        else:
            return n
    
    def result_format(v):
        m = v // 60
        s = v % 60
        return f'{time_format(m)}:{time_format(s)}'
    
    video_len_value = time_value(video_len)
    pos_value = time_value(pos)
    op_start_value = time_value(op_start)
    op_end_value = time_value(op_end)
    
    def c_skip(v):
        if op_start_value <= v <= op_end_value:
            return op_end_value
        else:
            return v
    
    def c_prev(v):
        v = c_skip(v)
        v -= 10
        
        if v <= 0:
            return 0
        else:
            return c_skip(v)
            
    def c_next(v):
        v = c_skip(v)
        v += 10
        
        if v >= video_len_value:
            return video_len_value
        else:
            return c_skip(v)
    
    commands_dict = {
        'prev': c_prev,
        'next': c_next,
        'skip': c_skip 
    }
    
    for c in commands:
        pos_value = commands_dict[c](pos_value)

    return result_format(pos_value)