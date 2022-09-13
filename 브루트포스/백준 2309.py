heights = [int(input())for _ in range(9)]
sum1 = sum(heights)
def answer(heights):
    for i in range(9):
        sum2 = sum1 - heights[i]
        for j in range(i+1, 9):
            sum2 -= heights[j]
            if sum2 == 100:
                x = heights[i]
                y = heights[j]
                heights.remove(x)
                heights.remove(y)
                return sorted(heights)
            else:
                sum2 = sum1 - heights[i]

result = answer(heights)
print(*result, sep = '\n')
