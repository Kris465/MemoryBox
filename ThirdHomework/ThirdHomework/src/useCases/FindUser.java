package useCases;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

import javax.sound.sampled.AudioFormat.Encoding;

public class FindUser {

    public void findUser() {
        Scanner scanner = new Scanner(System.in, "UTF-8");
        System.out.println("Введите фамилию пользователя");
        String lastName = scanner.nextLine();

        File file = new File(lastName + ".txt");
        if (!file.exists()) {
            System.out.println("Пользователь с такой фамилией не найден");
            return;
        }

        try {
            Scanner fileScanner = new Scanner(file,"UTF-8");
            while (fileScanner.hasNextLine()) {
                String userData = fileScanner.nextLine();
                String[] userDataArray = userData.split(" ");
                System.out.println("Фамилия: " + userDataArray[0]);
                System.out.println("Имя: " + userDataArray[1]);
                System.out.println("Отчество: " + userDataArray[2]);
                System.out.println("Дата рождения: " + userDataArray[3]);
                System.out.println("Номер телефона: " + userDataArray[4]);
                System.out.println("Пол: " + userDataArray[5]);
                System.out.println("--------------------");
            }
        } catch (FileNotFoundException e) {
            System.out.println("Ошибка при чтении файла пользователя");
        }
    }
}
