# Создайте программу для игры в ""Крестики-нолики"".



def find_index(new_board, num):
    if isinstance(new_board, (list, tuple)):
        for i, elem in enumerate(new_board):
            index_ = find_index(elem, num)
            if index_ != None:
                return (i,) + index_
    elif new_board == num:
        return tuple()
    return None

def tic_tac_toe():
    print("Hello! Let's play tic_tac_toe!")

    board = [[-1, -1, -1], 
            [-1, -1, -1],
            [-1, -1, -1]]

    sign = input("Would you like X or O? Input your choice: ")
    if sign == "X":
        flag = True
        sign = 1
    else: 
        flag = False
        sign = 0

    i = 0

    while i < 9:
        if flag == True:
            line = int(input("Input the line: "))
            column = int(input("Input column: "))
            board[line - 1][column - 1] = sign
            flag = False
        else:
            print("Ok, it's my turn.")
            index_is = find_index(board, -1)
            line = int(index_is[0])
            column = int(index_is[1])
            if sign == 0:
                board[line][column] = 1
            else: board[line][column] = 0
            flag = True
            
        for row in board:
            for elem in row:
                if elem == 0:
                    elem = "O"
                elif elem == 1:
                    elem = "X"
                else: elem = "_"
                print(elem, end=' ')
            print()
        
        i += 1
    
tic_tac_toe()