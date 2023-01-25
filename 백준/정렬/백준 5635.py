n = int(input())

students = [input().split() for _ in range(n)]

students.sort(key = lambda x: (x[3], int(x[2]), int(x[1])))

print(students[-1][0], students[0][0], sep = '\n')