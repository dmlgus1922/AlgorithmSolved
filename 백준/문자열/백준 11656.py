string = input()

words = [string[i:] for i in range(len(string))]

print(*sorted(words), sep='\n')