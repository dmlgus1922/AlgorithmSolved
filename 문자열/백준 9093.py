for _ in range(int(input())):
    sentence = input().split()
    r_sentence = ' '.join([s[::-1] for s in sentence])
    print(r_sentence)