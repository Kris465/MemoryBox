import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Input the first number: ");
        double num1 = scanner.nextDouble();
        System.out.print("Input the second number: ");
        double num2 = scanner.nextDouble();
        System.out.println("Sumup: " + (num1 + num2));
    }
}