package Workshop4;

import java.util.LinkedList;
import java.util.Scanner;

public class task3 {
    public static void main(String[] args) {
        // Заполнить и найти сумму четных параметров списка
        LinkedList<Integer> integerLinkedList = new LinkedList<>();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        while (n != 0) {
            integerLinkedList.add(n);
            n = scanner.nextInt();
        }

        for (int i = 1; i < integerLinkedList.size(); i++) {
            if (integerLinkedList.get(i) < 0) {
                integerLinkedList.remove(i);
                i--;
            }
        }
        System.out.println("list is " + integerLinkedList);
        scanner.close();
    }
}
