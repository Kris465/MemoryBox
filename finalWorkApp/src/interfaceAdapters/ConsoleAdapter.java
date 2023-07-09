package interfaceAdapters;

import java.util.Scanner;

import domain.CurrentAnimal;

public class ConsoleAdapter {
    private Scanner scanner;
    private CurrentAnimal currentAnimal;

    public ConsoleAdapter() {
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
                    AddAnimal();
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
}
