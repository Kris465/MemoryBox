def the_reader(participants, numreader):


    for _ in range(len(participants)):
        number_of_participants = len(participants)
        if num_reader % number_of_participants == 0:
            index_deleted = (num_reader % number_of_participants)
            func_print(participants, index_deleted)
            del participants[index_deleted - 1]
            stop_game = len(participants)
            if stop_game == 1:
                print(f'\nОстался человек под номером {participants[0]}')
                return
        else:
            index_deleted = (num_reader % number_of_participants)
            func_print(participants, index_deleted)
            del participants[index_deleted - 1]
            participants = participants[index_deleted - 1:] + participants[:index_deleted - 1]
            stop_game = len(participants)
            if stop_game == 1:
                print(f'\nОстался человек под номером {participants[0]}')
                return


def func_print(participants, index_deleted):
    print(
        f'\nТекущий круг людей: {sorted(participants)}\nНачало счета с номера {participants[0]}\nВыбывает человек под '
        f'номером {participants[index_deleted - 1]}')

count_participants = int(input('Сколько человек участвует: '))
participants = list(range(1, count_participants + 1))
num_reader = int(input('Число в считалке '))

the_reader(participants, num_reader)