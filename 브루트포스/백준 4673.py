numbers = set(range(1, 10001)) #1~10000의 세트.
strList = list() #문자열로 담을 리스트
notSelfNumber = set() #중복제거용 세트

for num in range(10001): 
    num = str(num) #문자열로 변환
    strList.append(num) #리스트에 저장
    num = int(num) #다시 정수로 변환
    for j in strList[num]: #문자열이 된 num의 각 자릿수를 num에 더해줌
        num += int(j)
    notSelfNumber.add(num) #그렇게 더해진 num을 세트에 저장

#세트끼리 연산해 차집합(=셀프넘버)을 구한다
selfNumber = sorted(numbers - notSelfNumber)

print(*selfNumber,sep = '\n')
