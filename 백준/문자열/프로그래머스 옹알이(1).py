def solution(babbling):
    saying = ["aya", "ye", "woo", "ma"]
    
    count = 0
    
    for word in babbling:
        for s in saying:
            while s in word:
                word = word.replace(s, '0')
        if word.isdigit():
            count += 1
    
    return count