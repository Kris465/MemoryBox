def id_():
    id_note = int(input("Input id of the note\n"))
    
    if id_note > 0:
        return id_note
    else:
        print("Sorry, I can't find nothing. For the first note:")
        return 1


def output(value):
    print(value)


def note():
    name = input("Input the title:\n")
    body = input("Input the message:\n")
    return name, body


def help():
    answer = input("Have you lost file 'notes.json'? yes/no\n")
    if answer == 'yes':
        return True
    else:
        return False

def start_menu():
    option = int(input("1. Read all\n2. Read a note\n3. Add\n4. Edit\n5. Delete\n6. HELP!\n7. Exit\n"))
    if option in [1, 2, 3, 4, 5, 6, 7]:
        return option
    else: print("Sorry, can you repeat, please?")

def id_or_time():
    opt = int(input("How would you like to see notes? id (1) or time (2)?\n"))
    if opt == 1:
        return True
    else: return False
