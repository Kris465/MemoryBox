package Homework4;

    // 1) Вывести список на экран в перевернутом виде (без массивов)
    // Пример:
    // 1 -> 2->3->4
    // Вывод:
    // 4->3->2->1

import java.util.LinkedList;
import java.util.Scanner;

public class task1 {
    public static void main(String[] args) {
        LinkedList<Integer> integerLinkedList = new LinkedList<>();
        System.out.println("Input the size of your list: ");
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println("Input the values of your list: ");
        for (int i = 0; i < n; i++) {
            integerLinkedList.add(scanner.nextInt());
        }
        scanner.close();
        for (int i = n - 1; i >= 0; i--) {
            System.out.print(integerLinkedList.get(i));
        }        
    }
}
