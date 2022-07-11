'''
도어락을 구매한 엘리스와 체셔가 둘의 태어난 년도를 뒤집어 더하여 그것을 비밀번호로 설정하려 한다.
둘의 태어난 년도가 주어질 때 답을 출력하는 프로그램이다.

입력 예)
1995 2000
출력 예)
5993
'''
cat, rabbit = map(int, input().split())
password = int(str(cat)[::-1]) + int(str(rabbit)[::-1])
print(password)