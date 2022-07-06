days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
x, y = map(int, input().split())

day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = (sum(day[:x]) + y) % 7
print(days[day-1])
