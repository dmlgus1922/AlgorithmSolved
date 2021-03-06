'''
김박사는 데이터가 유출되지 않기 위해 암호를 만들기로 했다.
모든 데이터는 40자리의 숫자로 변환해 저장했고 암호를 만드는 방법은 다음과 같다.
1. 모든 데이터를 더한다.
2. 더한 수의 앞에서부터 열 개의 자릿수를 체크 암호로 사용한다.

입력)
첫 번째 줄에 김박사가 저장할 데이터의 수(n)를 입력한다.
다음 n개의 줄에 40자리의 숫자를 입력한다.

출력)
입력 데이터로 만들어진 체크 암호를 출력한다.
'''
n = int(input())
data = [int(input()) for _ in range(n)]

ck = str(sum(data))
print(ck[:10])
