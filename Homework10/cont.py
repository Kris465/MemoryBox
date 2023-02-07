def controller(string, in_board):
    try: 
        string = int(string)
    except:
        string = string

    if isinstance(string, str):
        message, use_sign, bot_sign, refreshed_board = sign_choose(string)
        return [message, refreshed_board]
    elif isinstance(string, int):
        return tic_tac_toe(string, use_sign, bot_sign, in_board)
    else: return "Your input was incorrect, try again."