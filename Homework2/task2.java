package Homework2;

// 2) Дана последовательность целых чисел, оканчивающаяся нулем. Найти сумму положительных чисел, после которых следует отрицательное число.

import java.util.Scanner;

public class task2 {
    public static void main(String[] args) {
        int a, b, sum = 0, n;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Input the length of number sequence: ");
        n = scanner.nextInt();
        System.out.println("Thank you, now input your sequence: ");

        a = scanner.nextInt();
        for (int i = 1; i < n; i++) {
            b = scanner.nextInt();
            if (a > 0 & b < 0) {
                sum += a;
            }
            a = b;
        }
        System.out.println("Summa is: " + sum);
        scanner.close(); // нужен цикл while, по 0 прекращаем ввод, переделать
    }
}
