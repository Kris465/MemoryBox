import magic_box

def controller(string):
    try: 
        string = int(string)
    except:
        string = string

    if isinstance(string, str):
        message = sign_choose(string)
        return message
    elif isinstance(string, int):
        message = tic_tac_toe(string)
    else: 
        message = "Your input was incorrect, try again."

    return message

def sign_choose(user_string):
    lst = magic_box.take()
    print(lst, type(lst))

    if user_string == "X":
        lst[1] = "X"
        lst[2] = "O"
    else: 
        lst[1] = "O"
        lst[2] = "X"
        tic_tac_toe("STRING")

    magic_box.put(lst)

    return "Got it!"

def tic_tac_toe(user_string):
    lst = magic_box.take()
    temp_board = [ch for ch in lst[0]]
    user_sign = lst[1]
    my_sign = lst[2]

    try:
        user_string = int(user_string)
    except:
        user_string = user_string

    if isinstance(user_string, int):
        lst[0] = temp_board.insert(user_string - 1, user_sign)
        won = win_check()
        if lst[3]:
            message = f"Congradulation! {won} has won!"
        else:
            for i in range(len(temp_board)):
                if isinstance(temp_board[i], int):
                    temp_board.insert(i, my_sign)
                else: continue
    else:
        temp_board.insert(4, my_sign)
    
    lst[0] = temp_board
    
    magic_box.put(lst)
        
    message = "Your turn"
    return message


def win_check():
    lst = magic_box.take()
    in_board = [ch for ch in lst[0]]
    
    if (in_board[0] == in_board[1] == in_board[2]) or (in_board[0] == in_board[3] == in_board[6]) or (in_board[0] == in_board[4] == in_board[8]):
        winning = True
        win_sign = in_board[0]
    elif (in_board[3] == in_board[4] == in_board[5]) or (in_board[1] == in_board[4] == in_board[7]) or (in_board[2] == in_board[4] == in_board[6]):
        winning = True
        win_sign = in_board[4]
    elif (in_board[6] == in_board[7] == in_board[8]) or (in_board[2] == in_board[5] == in_board[8]):
        winning = True
        win_sign = in_board[8]
    else: 
        winning = False

    lst[3] = winning
    magic_box.put(lst)
    
    if winning:
        return win_sign
    else: "sorry"
