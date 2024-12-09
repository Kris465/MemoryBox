package diploma.task2;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        NoteManager noteManager = new NoteManager("notes.txt");

        while (true) {
            System.out.println("1. Add a note");
            System.out.println("2. Show notes");
            System.out.println("3. Exit");
            System.out.print("Choose an action: ");
            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1 -> {
                    System.out.print("The title of a note: ");
                    String title = scanner.nextLine();
                    System.out.print("The body of the note: ");
                    String content = scanner.nextLine();
                    noteManager.addNote(new Note(title, content));
                }
                case 2 -> {
                    for (Note note : noteManager.getNotes()) {
                        System.out.println(note);
                    }
                }
                case 3 -> {
                    System.out.println("Exiting...");
                    scanner.close();
                    return;
                }
                default -> System.out.println("Something went wrong. Try again.");
            }
        }
    }
}
