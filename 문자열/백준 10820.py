while True:
    try:
        lower = 0
        upper = 0
        number = 0
        blank = 0

        for s in input():
            if s.islower():
                lower += 1
            elif s.isupper():
                upper += 1
            elif s.isdigit():
                number += 1
            else:
                blank += 1
        print(lower, upper, number, blank)
    except EOFError:
        break
