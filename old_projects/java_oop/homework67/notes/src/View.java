import java.util.List;
import java.util.Scanner;

public class View {

    private Controller controller;
    
    public View(Controller controller) {
        this.controller = controller;
    }

    public void run() {
        Commands com = Commands.NONE;
    
    while (true) {
        String command = prompt("Input you command: ");
        com = Commands.valueOf(command);
        if (com == Commands.EXIT) return;
        String id;
        switch (com) {
            case CREATE:
                String title = prompt("Title: ");
                String text = prompt("Text: ");
                controller.saveNote(new Note(title, text));
                break;
            case READ:
                id = prompt("Id: ");
                try {
                    Note note = controller.readNote(id);
                    System.out.println(note);
                } catch (Exception e) {
                    throw new RuntimeException(e);
                }
                break;
            case DELETE:
                id = prompt("Id: ");
                try {
                    controller.deleteNote(id);
                    System.out.println("The note was removed.");
                } catch (Exception e) {
                    throw new RuntimeException(e);
                }
                break;
            case SHOW:
                List<Note> notes = controller.show();
                for (Note note : notes) {
                    System.out.println(note);
                }
                break;
            case EDIT:
                id = prompt("Id: ");
                String message = prompt("New Text: ");
                try {
                    controller.editNoteText(id, message);
                } catch (Exception e) {
                    throw new RuntimeException(e);
                }
                break;
            }
        }
    }

    private String prompt(String message) {
        Scanner in = new Scanner(System.in);
        System.out.print(message);
        return in.nextLine();
    }
}
