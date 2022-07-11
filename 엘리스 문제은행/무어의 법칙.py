'''
무어의 법칙에 의해 증가한 마이크로칩의 성능을 각 자릿수를 더하는 문제이다.
입력 예)
14
출력 예)
22
'''
print(sum(list(map(int,list(str(2**int(input())))))))