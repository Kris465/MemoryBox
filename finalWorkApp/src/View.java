import java.util.Scanner;

public class View {
    private Controller controller;
    private Scanner scanner;

    public View(Controller controller) {
        this.controller = controller;
        this.scanner = new Scanner(System.in);
    }

    public void displayMenu() {
        System.out.println("Welcome to the Animal Registry!");
        System.out.println("1. Show animal list");
        System.out.println("2. Show animal skills");
        System.out.println("3. Create new animal");
        System.out.println("4. Train animal with new skill");
        System.out.println("0. Exit");
    }

    public void start() {
        int choice;
        do {
            displayMenu();
            choice = getUserChoice();
            switch (choice) {
                case 1:
                    controller.showAnimalList();
                    break;
                case 2:
                    controller.showAnimalSkills();
                    break;
                case 3:
                    createNewAnimal();
                    break;
                case 4:
                    trainAnimalWithNewSkill();
                    break;
                case 0:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 0);
    }

    private int getUserChoice() {
        System.out.print("Enter your choice: ");
        return scanner.nextInt();
    }

    private void createNewAnimal() {
        scanner.nextLine();
        System.out.print("Enter the name of the animal: ");
        String name = scanner.nextLine();
        controller.createAnimal(name);
    }

    private void trainAnimalWithNewSkill() {
        scanner.nextLine();
        System.out.print("Enter the name of the animal: ");
        String name = scanner.nextLine();
        System.out.print("Enter the new skill: ");
        String skill = scanner.nextLine();
        controller.trainAnimal(name, skill);
    }
}
