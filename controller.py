import editing
import reading
import adding
import deleting

def user_menu():
    value = int(input("1. Read\n2. Add\n3. Edit\n4. Delete\n"))
    
    match value:
        case 1:
            id_note = int(input("Input id of your wished note otherwise input 0\n"))
            reading.read(id_note)
        case 2:
            name = input("Input the title of the note\n")
            body = input("Input the message\n")
            adding.add_(name, body)
        case 3:
            id_note = int(input("Input id of the note you would like to edit.\n"))
            editing.edit(id_note)
        case 4:
            deleting.delete()

