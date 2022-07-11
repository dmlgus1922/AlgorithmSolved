'''
A에서 출발해 B,C,D를 들러 다시 A로 돌아오는 엘리스 토끼는 고장이 나서 
초침으로만 움직이는 시계를 들고 이동을 한다.
각 지점에서 다음 지점으로 움직이는 데에 걸리는 시간이 주어질 때 총 걸린 시간을 분, 초로 출력하는 문제이다.

입력 예)
100
200
300
400
출력 예)
16
40
'''

time = sum([int(input()) for _ in range(4)])
minutes = time // 60
seconds = time % 60
print(minutes, seconds, sep = '\n')