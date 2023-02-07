def win_check(in_board):
    indexes = []
    in_board = in_board

    for i in range(len(in_board)):
            if isinstance(in_board[i], str):
                indexes.append(i)
    
    if in_board[0] == in_board[1] == in_board[2]:
        return True, in_board[0]
    elif in_board[0] == in_board[3] == in_board[6]:
        return True, in_board[0] 
    elif in_board[0] == in_board[4] == in_board[8]:
        return True, in_board[0]
    elif in_board[3] == in_board[4] == in_board[5]:
        return True, in_board[3]
    elif in_board[1] == in_board[4] == in_board[7]:
        return True, in_board[1]
    elif in_board[2] == in_board[4] == in_board[6]:
        return True, in_board[2]
    elif in_board[6] == in_board[7] == in_board[8]:
        return True, in_board[6]
    elif in_board[2] == in_board[5] == in_board[8]:
        return True, in_board[2]
    else: 
        return False, "sorry"