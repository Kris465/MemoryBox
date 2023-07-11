import java.util.List;
import java.util.Scanner;

public class View {
    private Controller controller;
    
    public View(Controller controller) {
        this.controller = controller;
    }
    
    public void menu() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("Menu:");
            System.out.println("1 - Add an animal");
            System.out.println("2 - Show all animals");
            System.out.println("0 - Exit");
            int choice = scanner.nextInt();
            scanner.nextLine();
            switch (choice) {
                case 1:
                    controller.addAnimal();
                    break;
                case 2:
                    controller.showAllAnimals();
                    break;
                case 0:
                    return;
                default:
                    System.out.println("Menu doesn't have such option.");
            }
        }
    }
    
    private void actionsWithAnimal() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the animal's name: ");
        String name = scanner.nextLine();
        
        Animal animal = controller.getAnimalByid(animal.id);
        if (animal == null) {
            System.out.println("Animal not found.");
            return;
        }
        
        while (true) {
            System.out.println("Actions with animal:");
            System.out.println("1 - Change animal's type");
            System.out.println("2 - Show animal's skills");
            System.out.println("3 - Teach new skill");
            System.out.println("0 - Back to main menu");
            
            int choice = scanner.nextInt();
            scanner.nextLine();
            
            switch (choice) {
                case 1:
                    changeAnimalType(animal);
                    break;
                case 2:
                    showAnimalSkills(animal);
                    break;
                case 3:
                    teachNewSkill(animal);
                    break;
                case 0:
                    return;
                default:
                    System.out.println("Menu doesn't have such option.");
            }
        }
    }
    
    private void changeAnimalType(Animal animal) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the new type of the animal: ");
        String newType = scanner.nextLine();
        animal.setType(newType);
    }
    
    private void showAnimalSkills(Animal animal) {
        List<String> skills = animal.getSkills();
        System.out.println("Animal's skills:");
        for (String skill : skills) {
            System.out.println(skill);
        }
    }
    
    private void teachNewSkill(Animal animal) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the new skill: ");
        String newSkill = scanner.nextLine();
        animal.addSkill(newSkill);
    }
}
