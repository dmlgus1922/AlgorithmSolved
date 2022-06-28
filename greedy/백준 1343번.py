def poly(board):
    for i in range(len(board)):
        if not board[i]:
            continue
        length = len(board[i])
    
        if length == 2:
            board[i] = 'BB'
        
        elif length % 4 == 0:
            board[i] = 'AAAA' * (length//4)

        elif length % 2 == 0:
            board[i] = 'AAAA' * (length//4) + 'BB'

        else:
            return -1
    return '.'.join(board)


board = input().split('.')
print(poly(board))
