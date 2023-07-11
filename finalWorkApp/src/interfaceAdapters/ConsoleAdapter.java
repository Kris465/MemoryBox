package interfaceAdapters;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import domain.CurrentAnimal;
import useCases.AddAnimal;
import useCases.EditAnimalType;
import useCases.TeachAnimal;

public class ConsoleAdapter {
    private Scanner scanner;
    private AddAnimal addAnimal;
    private EditAnimalType editAnimalType;
    private TeachAnimal teachAnimal;

    

    public ConsoleAdapter(AddAnimal addAnimal, EditAnimalType editAnimalType, TeachAnimal teachAnimal) {
        scanner = new Scanner(System.in);
        this.addAnimal = addAnimal;
        this.editAnimalType = editAnimalType;
        this.teachAnimal = teachAnimal;
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
                Scanner scanner = new Scanner(System.in);
                System.out.print("Введите id: ");
                int id = scanner.nextInt();
                System.out.print("Введите имя: ");
                String name = scanner.next();
                System.out.print("Введите возраст: ");
                int age = scanner.nextInt();
                System.out.print("Введите тип: ");
                String type = scanner.next();
                System.out.print("Введите количество навыков: ");
                int numSkills = scanner.nextInt();
        
                String[] skills = new String[numSkills];
                for (int i = 0; i < numSkills; i++) {
                    System.out.print("Введите навык " + (i+1) + ": ");
                    skills[i] = scanner.next();
                }
                CurrentAnimal currentAnimal = new CurrentAnimal(id, name, age, type, skills);
                    break;
                case 2:
                    // Установить тип животного
                    break;
                case 3:
                    // Показать список команд, которое животное умеет делать
                    break;
                case 4:
                    // Научить новой команде
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
