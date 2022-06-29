i = 1 #시나리오 번호
while True:
    n = int(input())

    if not n: #n이 0일 때 종료
        break
    
    students = {} #{학생번호: 학생이름}
    for key in range(1, n+1): #학생 번호는 1번부터 시작, n개 저장
        students[key] = input() 

    numbers = []
    for _ in range(2 * n - 1): #무조건 한 명만 못 받음. 2*n-1번 반복. 문제에도 명시됨
        number = int(input().split()[0]) #입력받는 문자열 중 뒤 알파벳은 크게 상관이 없는 것 같다. 숫자만 입력받아서 정수로 변환
        if number in numbers: #이미 리스트 내에 번호가 있다면 돌려받는 것이므로 지워준다
            numbers.remove(number)
        else:  #리스트 내에 번호가 없을 땐 뺏기는 중이므로 넣어준다.
            numbers.append(number)

    #반복문이 끝나면 돌려받지 못한 학생의 번호 하나만 남을 터
    
    print(i, students[numbers[0]]) #시나리오 번호, 학생 이름
    i += 1 #시나리오 번호 증가
