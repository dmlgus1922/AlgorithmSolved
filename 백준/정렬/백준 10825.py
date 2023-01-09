n = int(input())

students = []

for _ in range(n):
    info = input().split()
    
    student = [info[0]]
    score = list(map(int, info[1:]))
    
    student.extend(score)
    students.append(student)
    
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

answer = [x[0] for x in students]

print(*answer, sep = '\n')
