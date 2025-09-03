package Lectures;
import java.util.Scanner;

public class Lec3Name {
    public static void main(String[] args) {
        Scanner iScanner = new Scanner(System.in);
        System.out.printf("name: ");
        String name = iScanner.nextLine();
        System.out.printf("Hello, %s!", name);
        iScanner.close();
    }
}
