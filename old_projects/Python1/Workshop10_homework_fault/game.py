board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def controller(string, in_board):
    try: 
        string = int(string)
    except:
        string = string

    use_sign, bot_sign = "l", "l"

    if isinstance(string, str):
        message, use_sign, bot_sign, refreshed_board = sign_choose(string)
        return [message, refreshed_board]
    elif isinstance(string, int):
        return tic_tac_toe(string, use_sign, bot_sign, in_board)
    else: return "Your input was incorrect, try again."


def sign_choose(user_string):
    fstep_board = board

    if user_string == "X":
        user_sign = "X"
        my_sign = "O"
    else: 
        user_sign = "O"
        my_sign = "X"
        temp, fstep_board = tic_tac_toe("first_step", user_sign, my_sign, fstep_board)

    return "Got it!", user_sign, my_sign, fstep_board

def tic_tac_toe(inf, user_sign, my_sign, in_board):
    refreshed_board = in_board
    try:
        inf = int(inf)
    except:
        inf = inf

    if isinstance(inf, int):
        refreshed_board = in_board.insert(inf - 1, user_sign)
        won, winning_sign = win_check(refreshed_board)
        if won:
            return f"Congradulation! {winning_sign} has won!"
        else:
            for i in range(len(refreshed_board)):
                if isinstance(refreshed_board[i], int):
                    refreshed_board.insert(i, my_sign)
                else: continue
    else:
        refreshed_board.insert(4, my_sign)
        
    return "Your turn", refreshed_board


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
