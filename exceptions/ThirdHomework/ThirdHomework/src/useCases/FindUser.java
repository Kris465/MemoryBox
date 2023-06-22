package useCases;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class FindUser {

    public void findUser() {
        Scanner scanner = new Scanner(System.in, "UTF-8");
        System.out.println("Input the user's surname");
        String surname = scanner.nextLine();

        File file = new File(surname + ".txt");
        if (!file.exists()) {
            System.out.println("There isn't user with this surname");
            return;
        }

        try {
            Scanner fileScanner = new Scanner(file,"UTF-8");
            while (fileScanner.hasNextLine()) {
                String userData = fileScanner.nextLine();
                String[] userDataArray = userData.split(" ");
                System.out.println("Surname: " + userDataArray[0]);
                System.out.println("Name: " + userDataArray[1]);
                System.out.println("Patronymic: " + userDataArray[2]);
                System.out.println("Date of Birth: " + userDataArray[3]);
                System.out.println("Phone number: " + userDataArray[4]);
                System.out.println("Gender: " + userDataArray[5]);
                System.out.println("--------------------");
            }
        } catch (FileNotFoundException e) {
            System.out.println("Error with reading a file");
        }
    }
}
