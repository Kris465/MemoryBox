package Homework2;

// 3) Дана последовательность N целых чисел. Найти сумму простых чисел.

import java.util.Scanner;

public class task3 {
    public static void main(String[] args) {
        int a, sum = 0, n;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Input the length of number sequence: ");
        n = scanner.nextInt();
        System.out.println("Thank you, now input your sequence: ");

        for (int i = 1; i <= n; i++) {
            a = scanner.nextInt();
            sum += a;
            if (a > 0) {
                for (int k = 2; k <= Math.sqrt(a); k++) {
                    if (a % k == 0) {
                        sum -= a;
                        break;
                    }
            }} else {
                sum -= a;
            }
        }
        System.out.println("Summa is: " + sum);
        scanner.close();
    }
}
