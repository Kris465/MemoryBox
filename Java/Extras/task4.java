package Extras;
import java.util.Scanner;

public class task4 {
    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        int first, second, result;
        System.out.print("Input the first number: ");
        first = num.nextInt();
        System.out.print("Input the second number: ");
        second = num.nextInt();
        result = first + second;
        System.out.println("Your result is: " + result);
        num.close();
    }
}
