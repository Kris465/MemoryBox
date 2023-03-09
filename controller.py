import editing
import reading
import adding
import deleting
import zero_note
import menu

def logic():
    while True:
        value = menu.start_menu()
    
        match value:
            case 1:
                menu.output(reading.read_all())
            case 2:
                menu.output(reading.read_one())
            case 3:
                adding.add_(menu.note())
            case 4:
                editing.edit(menu.id_(), menu.note())
            case 5:
                deleting.delete(menu.id_())
            case 6:
                if menu.help():
                    zero_note.sample_()
                else: continue
            case 7:
                break
