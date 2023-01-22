ag1, ag2, ag3 = [int(input()) for _ in range(3)]

if ag1 + ag2 + ag3 != 180:
    print('Error')
elif ag1 == ag2 == ag3:
    print('Equilateral')
elif ag1 == ag2 or ag1 == ag3 or ag2 == ag3:
    print('Isosceles')
else:
    print('Scalene')