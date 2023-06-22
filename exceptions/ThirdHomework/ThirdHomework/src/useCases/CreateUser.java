package useCases;

import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

import domain.User;

public class CreateUser {

    public static void createUser() {
        Scanner scanner = new Scanner(System.in, "UTF-8");
        System.out.println("Enter user data in the following format: Surname Name Patronymic Birthday (dd.mm.yyyy) PhoneNumber (10) Gender");
        String input = scanner.nextLine();
        String[] userDataArray = input.split(" ");
        if (userDataArray.length != 6) {
            System.out.println("One of fields is empty.");
            createUser();
            return;
        }
        User user = new User();

        for (String data : userDataArray) {
            try {
                if (data.matches("[a-zA-Zа-яА-Я]+") && !data.equals("f") && !data.equals("m")) {
                    if (data.equals(userDataArray[0])) {
                        user.setSurname(data);
                    } else if (data.equals(userDataArray[1])) {
                        user.setName(data);
                    } else {
                        user.setPatronymic(data);
                    }
                } else if (data.matches("\\d{2}\\.\\d{2}\\.\\d{4}")) {
                    LocalDate dateOfBirth = LocalDate.parse(data, DateTimeFormatter.ofPattern("dd.MM.yyyy"));
                    user.setDateOfBirth(dateOfBirth);
                } else if (data.matches("\\d{10}")) {
                    user.setPhoneNumber(data);
                } else if (data.matches("[mf]")) {
                    user.setGender(data.charAt(0));
                } else {
                    System.out.println("Incorrect input. Try again.");
                    createUser();
                    return;
                }
            } catch (Exception e) {
                System.out.println("Try again.");
            }
        }

        try (FileWriter writer = new FileWriter(user.getSurname() + ".txt", true)) {
            writer.write(user.toString() + "\n");
            System.out.println("User has been added to the file.");
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }
    } 
}
