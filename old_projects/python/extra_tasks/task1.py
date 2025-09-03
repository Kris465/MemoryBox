# ; 4 - По кругу стоят n человек. Ведущий посчитал m человек по кругу, 
# ; начиная с первого. При этом каждый из тех, кто участвовал в этом счете,
# ; получил по одной монете, остальные получили по две монеты. Далее человек,
# ; на котором остановился счет, отдает все свои монеты следующему по счету человеку,
# ; а сам выбывает из круга. Процесс продолжается с места остановки аналогичным образом 
# ; до последнего человека в круге. Составьте алгоритм, который проводит эту игру. 
# ; Если хотите делать паузы, то импортируйте библиотеку time и используйте оттуда 
# ; функцию sleep. Определите номер этого человека и количество монет,
# ;  которые оказались у него в конце игры.

def user_input():
    number = int(input("Input the number of players: "))
    m_pos = int(input("Input the amount: "))

    return number, m_pos

def first_step(number):
    lst = []
    for i in range(number):
        lst.append(i + 1)
    
    dictionary_play = dict.fromkeys(lst)

    return dictionary_play

def game(dictionary_play, m_pos):
    coin = 1

    for k in dictionary_play:
        if k < m_pos:
            dictionary_play[k] = coin
        elif k == m_pos:
            dictionary_play[k] = coin + 1
            winning = dictionary_play.get(m_pos)
            dictionary_play[k] = 0
        elif k == m_pos + 1:
            dictionary_play[k] = coin + 1 + winning
        else:
            dictionary_play[k] = coin + 1

    return dictionary_play

time = 2

def game_winner(dictionary_play, m_pos, time):

        new_dictionary = game_winner(game(dictionary_play, m_pos), m_pos, time)

        return new_dictionary, m_pos, time - 1
    

n, m = user_input()
dictionary = first_step(n)
game_winner(dictionary, m, 3)

    
