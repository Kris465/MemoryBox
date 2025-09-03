package Workshop2;

import java.util.Scanner;

public class task1 {
    public static void main(String[] args) {
        Double x;
        int n;
        double result;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Input the number: ");
        x = scanner.nextDouble();
        System.out.println("Input the pow of the previous number: ");
        n = scanner.nextInt();
        scanner.close();
        result = x;
        for (int i = 1; i < n; i++) {
            result *= x;
        }
        System.out.println("result = " + result);
    }

}
