package Homework2;

// 6) Дан массив целых чисел. Заменить отрицательные элементы на сумму индексов двузначных элементов массива.

import java.util.Scanner;

public class task6 {
    public static void main(String[] args) {
        int sum = 0;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Input the size of your array: ");
        int n = scanner.nextInt();
        int[] mass = new int[n];

        System.out.println("Thank you, input your array: ");
        for (int i = 0; i < n; i++) {
            mass[i] = scanner.nextInt();
            if (Math.abs(mass[i]) < 100 & Math.abs(mass[i]) > 10) {
                sum += i;
            }
            System.out.println("Summa of indexes is " + sum);
        }

        for (int i = 0; i < n; i++) {
            if (mass[i] < 0) {
                mass[i] = sum;
            }
            System.out.print(" " + mass[i]);
        }
        scanner.close();
    }
}
