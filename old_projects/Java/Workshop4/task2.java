package Workshop4;

import java.util.LinkedList;
import java.util.Scanner;

public class task2 {
    public static void main(String[] args) {
        // Заполнить и найти сумму четных параметров списка
        LinkedList<Integer> integerLinkedList = new LinkedList<>();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int sum = 0;
        while (n != 0) {
            if (n % 2 == 1) {
                sum += n;
            }
            integerLinkedList.add(n);
            n = scanner.nextInt();
        }

        for (int i = 0; i < integerLinkedList.size(); i++) {
            if (integerLinkedList.get(i) % 3 != 0) {
                integerLinkedList.set(i, sum);
            }
        }
        System.out.println("sum is " + sum + integerLinkedList);
        scanner.close();
    }
}
