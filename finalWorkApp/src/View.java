import java.util.List;
import java.util.Scanner;

public class View {
    private Controller controller;
    private Counter counter;

    public View(Controller controller, Counter counter) {
        this.controller = controller;
        this.counter = counter;

    }

    public void start() {
        Scanner scanner = new Scanner(System.in);
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
                    findAnimalMenu(scanner);
                    break;
                case 3:
                    addAnimalMenu(scanner);
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

    public void findAnimalMenu(Scanner scanner) {
        int id = Integer.parseInt(prompt(scanner, "Enter animal ID: "));
        
        Animal animal = controller.findAnimalById(id);
        
        if (animal != null) {
            animalDetailsMenu(animal, scanner);
        } else {
            System.out.println("Animal not found.");
        }
    }

    public void animalDetailsMenu(Animal animal, Scanner scanner) {
        int choice = 0;
        
        while (choice != 5) {
            System.out.println("Animal Details:");
            System.out.println("ID: " + animal.getId());
            System.out.println("Name: " + animal.getName());
            System.out.println("Type: " + animal.getType());
            System.out.println("Skills: " + animal.getSkills());
            System.out.println();
            System.out.println("1. Change animal type");
            System.out.println("2. View animal");
            System.out.println("3. Teach animal command");
            System.out.println("4. Back");
            System.out.print("Enter your choice: ");
            
            choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    changeAnimalTypeMenu(animal, scanner);
                    break;
                case 2:
                    viewAnimalMenu(animal);
                    break;
                case 3:
                    teachAnimalCommandMenu(animal, scanner);
                    break;
                case 4:
                    System.out.println("Returning to previous menu...");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        }
    }

    public void addAnimalMenu(Scanner scanner) {
        String name = prompt(scanner, "Enter animal name: ");
        int age = Integer.parseInt(prompt(scanner, "Enter animal age: "));
        String type = prompt(scanner, "Enter animal type: ");
        int id = counter.getNextId();

        Animal newAnimal = new Animal(id, name, type, age);
        controller.addAnimal(newAnimal);
        
        System.out.println("Animal added successfully.");
    }

    public void changeAnimalTypeMenu(Animal animal, Scanner scanner) {
        String newType = prompt(scanner, "Enter new animal type: ");
        controller.changeAnimalType(animal.getId(), newType);
        
        System.out.println("Animal type changed successfully.");
    }
    
    public void viewAnimalMenu(Animal animal) {
        System.out.println("Animal Details:");
        System.out.println("ID: " + animal.getId());
        System.out.println("Name: " + animal.getName());
        System.out.println("Type: " + animal.getType());
        System.out.println("Skills: " + animal.getSkills());
    }

    public void teachAnimalCommandMenu(Animal animal, Scanner scanner) {
        String command = prompt(scanner, "Enter new command: ");
        
        controller.teachAnimalCommand(animal.getId(), command);
        
        System.out.println("Animal command taught successfully.");
    }

    public String prompt(Scanner scanner, String text) {
        System.out.print(text);
        return scanner.nextLine();
    }
}
