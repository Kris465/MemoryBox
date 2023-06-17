package interfaceAdapters;

import java.util.Scanner;

import useCases.CreateUser;
import useCases.FindUser;

public class ConsoleAdapter {
    private final CreateUser createUser;
    private final FindUser findUser;

    public ConsoleAdapter(CreateUser createUser, FindUser findUser) {
        this.createUser = createUser;
        this.findUser = findUser;
    }

    public void start() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("Menu:");
            System.out.println("1 - Create user");
            System.out.println("2 - Find user");
            System.out.println("0 - Exit");

            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    createUser.createUser();
                    break;
                case 2:
                    findUser.findUser();
                    break;
                case 0:
                    return;
                default:
                    System.out.println("Menu doesn't have such option.");
            }
        }
    }
}
