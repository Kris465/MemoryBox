import editing
import reading
import adding
import deleting
import zero_note

def user_menu():
    value = int(input("1. Read\n2. Add\n3. Edit\n4. Delete\n5. HELP!\n"))
    
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
            name = input("What title would you like to see?\n")
            body = input("What message would you like to leave?\n")
            editing.edit(id_note, name, body)
        case 4:
            id_note = int(input("Input id of the note that you wish to delete.\n"))
            deleting.delete(id_note)
        case 5:
            answer = input("Have you lost file 'notes.json'? yes/no\n")
            if answer == 'yes':
                zero_note.sample_()
            else:
                print("Good luck!")
        