package useCases;

import java.io.BufferedWriter;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Scanner;

public class CreateUser {

    public void createUser() {
        Scanner scanner = new Scanner(System.in, "UTF-8");
        System.setProperty("console.encoding","UTF-8");
        System.out.println("Введите данные пользователя в формате: Фамилия Имя Отчество Дата рождения (ДД.ММ.ГГГГ) Номер телефона Пол");
        String userData = scanner.nextLine();

        String[] userDataArray = userData.split(" ");
        if (userDataArray.length != 6) {
            System.out.println("Некорректный формат данных. Введите данные в формате: Фамилия Имя Отчество Дата рождения (ДД.ММ.ГГГГ) Номер телефона Пол");
            createUser();
            return;
        }

        String surname = userDataArray[0];
        String firstName = userDataArray[1];
        String patronymic = userDataArray[2];
        String dateOfBirth = userDataArray[3];
        String phoneNumber = userDataArray[4];
        String gender = userDataArray[5];

        if (!isValidDate(dateOfBirth)) {
            System.out.println("Некорректный формат даты рождения. Введите дату в формате: ДД.ММ.ГГГГ");
            createUser();
            return;
        }

        if (!isValidPhoneNumber(phoneNumber)) {
            System.out.println("Некорректный формат номера телефона. Введите номер в формате: +7XXXXXXXXXX");
            createUser();
            return;
        }

        if (!isValidGender(gender)) {
            System.out.println("Некорректный формат пола. Введите пол в формате: m/f");
            createUser();
            return;
        }

        try {
            FileOutputStream fos = new FileOutputStream(surname + ".txt", true);
            OutputStreamWriter osw = new OutputStreamWriter(fos, "UTF-8");
            BufferedWriter writer = new BufferedWriter(osw);
            writer.write(surname + " " + firstName + " " + patronymic + " " + dateOfBirth + " " + phoneNumber + " " + gender + "\n");
            writer.close();
            System.out.println("Пользователь успешно создан");
        } catch (IOException e) {
            System.out.println("Ошибка при сохранении пользователя");
        }
    }

    private boolean isValidDate(String date) {
        String[] dateArray = date.split("\\.");
        if (dateArray.length != 3) {
            return false;
        }
        int day = Integer.parseInt(dateArray[0]);
        int month = Integer.parseInt(dateArray[1]);
        int year = Integer.parseInt(dateArray[2]);
        return day >= 1 && day <= 31 && month >= 1 && month <= 12 && year >= 1900 && year <= 2023;
    }

    private boolean isValidPhoneNumber(String phoneNumber) {
        return phoneNumber.matches("\\+7\\d{10}");
    }

    private boolean isValidGender(String gender) {
        return gender.equals("m") || gender.equals("f");
    }
}

