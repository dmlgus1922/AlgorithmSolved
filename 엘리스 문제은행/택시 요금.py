'''
엘리스는 하루 동안 같은 콜택시를 이용하려고 합니다. 
엘리스가 부를 수 있는 택시 회사는 삼보운수와 강남운수 인데, 
두 개의 택시 회사는 같은 거리를 가더라도 비용이 다릅니다.

두 회사의 비용을 계산하는 방법은 다음과 같습니다.

삼보운수의 택시 미터기는 100m마다 100원씩 금액이 올라갑니다.
강남운수의 택시 미터기는 200m마다 180원씩 금액이 올라갑니다.
예를 들어 삼보운수의 택시를 이용하면 0-99m 이동 시 100원이 부과되며, 
100-199m 이동 시 100원이 추가됩니다.

택시비를 절약하고 싶은 엘리스가 택시 회사를 적절하게 선택할 예정입니다. 
하루 동안 택시를 N 번 이용할 때, 택시 회사와 택시요금을 출력하는 프로그램을 작성하세요.


입력
첫 번째 줄에 엘리스가 하루 동안 택시를 이용할 횟수인 정수 N을 입력합니다.
(1≤N≤20)
두 번째 줄에 엘리스가 택시를 타고 한 번에 이동할 미터의 수를 공백을 간격으로 N개 입력합니다.
(1≤이동할 거리≤2000)

출력
첫 번째 줄에 엘리스가 결정한 택시회사의 이름(‘강남운수’ 또는 ‘삼보운수’)과 택시 금액을 공백으로 구분하여 출력합니다.
※엘리스는 금액이 동일하다면 ‘강남운수’를 이용합니다.

입력 예)
3
100 100 100

출력 예)
강남운수 540
'''
import math
n = int(input())
dist = list(map(int,input().split()))
def money(dist, meter):
    meterD = {99:100, 199:180}
    nameD = {99:'삼보운수', 199:'강남운수'}
    money = meterD[meter]
    name = nameD[meter]
    result = 0
    for d in dist:
        result += math.ceil(d / meter) * money
    return [name, result]
sambo = money(dist, 99)
kangnam = money(dist, 199)
if sambo == kangnam:
    print(kangnam[0], kangnam[1])
else:
    ans = min(sambo,kangnam,key=lambda x:x[1])
    print(ans[0],ans[1])
