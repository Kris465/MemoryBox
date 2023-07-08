import java.util.Scanner;

public class View {
    private Scanner scanner;
    private CurrentAnimal currentAnimal;

    public View() {
        scanner = new Scanner(System.in);
        currentAnimal = null;
    }

    public void showMenu() {
        System.out.println("Меню:");
        System.out.println("1. Создать животное");
        System.out.println("2. Присвоить тип животного");
        System.out.println("3. Посмотреть список команд, которые животное может выполнять");
        System.out.println("4. Обучить новой команде");
        System.out.println("0. Выход");
    }

    public void handleUserInput() {
        int choice = -1;
        while (choice != 0) {
            showMenu();
            System.out.print("Выберите пункт меню: ");
            choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    createAnimal();
                    break;
                case 2:
                    setAnimalType();
                    break;
                case 3:
                    showAnimalActions();
                    break;
                case 4:
                    trainNewCommand();
                    break;
                case 0:
                    System.out.println("Выход из программы");
                    break;
                default:
                    System.out.println("Некорректный выбор");
                    break;
            }
        }
    }

    private void createAnimal() {
        System.out.print("Введите имя животного: ");
        String name = scanner.next();
        System.out.print("Введите возраст животного: ");
        int age = scanner.nextInt();
        currentAnimal = new CurrentAnimal(name, age);
        System.out.println("Животное создано");
    }

    private void setAnimalType() {
        if (currentAnimal == null) {
            System.out.println("Животное не создано");
        } else {
            System.out.print("Введите тип животного: ");
            String type = scanner.next();
            currentAnimal.setType(type);
            System.out.println("Тип животного присвоен");
        }
    }

    private void showAnimalActions() {
        if (currentAnimal == null) {
            System.out.println("Животное не создано");
        } else {
            System.out.println("Список команд, которые животное может выполнять:");
            // Вывод списка команд, которые животное может выполнять
        }
    }

    private void trainNewCommand() {
        if (currentAnimal == null) {
            System.out.println("Животное не создано");
        } else {
            System.out.print("Введите новую команду: ");
            String command = scanner.next();
            // Обучение животного новой команде
        }
    }
}
