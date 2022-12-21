package Homework2;

// 4) Дана последовательность из N целых чисел. Верно ли, что последовательность является возрастающей.

import java.util.Scanner;

public class task4 {
    public static void main(String[] args) {
        int a, b, n;
        boolean green_flag = true;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Input the length of number sequence: ");
        n = scanner.nextInt();
        System.out.println("Thank you, now input your sequence: ");

        a = scanner.nextInt();
        for (int i = 1; i < n; i++) {
            b = scanner.nextInt();
            if (a > b) {
                green_flag = false;
            }
            a = b;
        }
        scanner.close();

        if (green_flag == true) {
            System.out.println("The sequence is ascending.");
        } else {
            System.out.println("The sequence isn't ascending.");
        }
    }
}
