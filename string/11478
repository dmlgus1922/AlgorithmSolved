string = input()

sPart = set()

x = 1
while x <= len(string):
    for i in range(len(string)):
        if i+x > len(string):
            continue
        sPart.add(string[i:i+x])
    x += 1   
    
print(len(sPart))
