def controller(mes, ch, lst):
    try:
        string = int(mes)
    except:
        string = mes

    if isinstance(string, str):
        message = sign_choose(ch)
        return message
    elif isinstance(string, int):
        lst[string - 1] = ch
        won, winning_sign = win_check(lst)
        if won:
            return(f"Congradulation! {winning_sign} has won!")
        else:
            my_sign = sign_choose(ch)
            for i in range(len(lst)):
                if isinstance(lst[i], int):
                    lst[i] = my_sign
                    break
        return lst
    else:
        message = "Your input was incorrect, try again."

    return message


def sign_choose(ch):
    print(ch, type(ch))

    if ch == "X":
        ch = "O"
    else:
        ch = "X"

    return ch


def win_check(lst):
    
    if (lst[0] == lst[1] == lst[2]) or (lst[0] == lst[3] == lst[6]) or (lst[0] == lst[4] == lst[8]):
        winning = True
        win_sign = lst[0]
    elif (lst[3] == lst[4] == lst[5]) or (lst[1] == lst[4] == lst[7]) or (lst[2] == lst[4] == lst[6]):
        winning = True
        win_sign = lst[4]
    elif (lst[6] == lst[7] == lst[8]) or (lst[2] == lst[5] == lst[8]):
        winning = True
        win_sign = lst[8]
    else: 
        winning = False
        win_sign = " "
    
    return (winning, win_sign)
