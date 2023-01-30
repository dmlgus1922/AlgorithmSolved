def solution(n):
    count = 0
    while True:
        if count == 500:
            return -1
        if n == 1:
            return count
        elif n % 2 == 0:
            n //= 2
        else:
            n *= 3
            n += 1
        count += 1