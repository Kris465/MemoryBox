import java.util.List;
import java.util.Scanner;

public class View {
    private Controller controller;
    private Scanner scanner;
    private Counter counter;

    public View(Controller controller, Counter counter) {
        this.controller = controller;
        this.scanner = new Scanner(System.in);
        this.counter = counter;

    }

    public void start() {
        int choice = 0;

        while (choice != 3) {
            System.out.println("Main Menu:");
            System.out.println("1. View all animals");
            System.out.println("2. Find animal");
            System.out.println("3. Add new animal");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");

            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    viewAllAnimalsMenu();
                    break;
                case 2:
                    findAnimalMenu();
                    break;
                case 3:
                    addAnimalMenu();
                case 4:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        }
    }

    public void viewAllAnimalsMenu() {
        List<String> animalInfo = controller.getAllAnimalsInfo();

        System.out.println("Animal List:");
        for (String info : animalInfo) {
            System.out.println(info);
        }
    }

    public void findAnimalMenu() {
        System.out.print("Enter animal ID: ");
        int id = scanner.nextInt();

        Animal animal = controller.findAnimalById(id);

        if (animal != null) {
            animalDetailsMenu(animal);
        } else {
            System.out.println("Animal not found.");
        }
    }

    public void animalDetailsMenu(Animal animal) {
        int choice = 0;

        while (choice != 5) {
            System.out.println("Animal Details:");
            System.out.println("ID: " + animal.getId());
            System.out.println("Name: " + animal.getName());
            System.out.println("Type: " + animal.getType());
            System.out.println("Skills: " + animal.getSkills());
            System.out.println();
            System.out.println("1. Add animal");
            System.out.println("2. Change animal type");
            System.out.println("3. View animal");
            System.out.println("4. Teach animal command");
            System.out.println("5. Back");
            System.out.print("Enter your choice: ");

            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    addAnimalMenu();
                    break;
                case 2:
                    changeAnimalTypeMenu(animal);
                    break;
                case 3:
                    viewAnimalMenu(animal);
                    break;
                case 4:
                    teachAnimalCommandMenu(animal);
                    break;
                case 5:
                    System.out.println("Returning to previous menu...");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        }
    }

    public void addAnimalMenu() {
        System.out.print("Enter animal name: ");
        scanner.nextLine();

        String name = scanner.nextLine();

        System.out.print("Enter animal age: ");
        int age = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Enter animal type: ");
        String type = scanner.nextLine();

        int id = counter.getNextId();
        Animal newAnimal = new Animal(id, name, type, age, null);
        controller.addAnimal(newAnimal);

        System.out.println("Animal added successfully.");
    }

    public void changeAnimalTypeMenu(Animal animal) {
        System.out.print("Enter new animal type: ");

        Thread inputThread = new Thread(() -> {
            String newType = scanner.nextLine();
            controller.changeAnimalType(animal.getId(), newType);
            System.out.println("Animal type changed successfully.");
        });

        inputThread.start();

        try {
            inputThread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void viewAnimalMenu(Animal animal) {
        System.out.println("Animal Details:");
        System.out.println("ID: " + animal.getId());
        System.out.println("Name: " + animal.getName());
        System.out.println("Type: " + animal.getType());
        System.out.println("Skills: " + animal.getSkills());
    }

    public void teachAnimalCommandMenu(Animal animal) {
        System.out.print("Enter new command: ");
        String command = scanner.nextLine();

        controller.teachAnimalCommand(animal.getId(), command);

        System.out.println("Animal command taught successfully.");
    }
}
