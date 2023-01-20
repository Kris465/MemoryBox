package Workshop2;

// 3)	Дан массив целых чисел. Найти количество пар соседних элементов, где первый элемент вдвое больше второго.

import java.util.Scanner;


public class task3 {
    public static void main(String[] args) {
        int k = 0;
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] mass = new int[n];

        for (int i = 1; i < n; i++) {
            mass[i] = scanner.nextInt();
        }

        for (int i = 0; i < n - 1; i++) {
            if(mass[i] == 2 * mass[i + 1]) {
                k++;
            }
        }
        System.out.println("k = " + k);
        scanner.close();
    }
}
