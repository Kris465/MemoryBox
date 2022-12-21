package Homework2;

// 5) Дан массив целых чисел. Найти сумму элементов, у которых последняя и предпоследняя цифры равны.

import java.util.Scanner;

public class task5 {
    public static void main(String[] args) {
        int sum = 0;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Input the size of your array: ");
        int n = scanner.nextInt();
        int[] mass = new int[n];

        System.out.println("Thank you, input your array: ");
        for (int i = 1; i < n; i++) {
            mass[i] = scanner.nextInt();
            if (mass[i] % 10 == (mass[i] / 10) % 10) {
                sum += mass[i];
            }
        }
        
        System.out.println("Sum = " + sum);
        scanner.close();
    }
}
