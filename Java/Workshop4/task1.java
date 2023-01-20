package Workshop4;

import java.util.LinkedList;
import java.util.Scanner;

public class task1 {
    public static void main(String[] args) {
        // Заполнить и найти сумму четных параметров списка
        LinkedList<Integer> integerLinkedList = new LinkedList<>();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for (int i = 0; i < n; i++) {
            integerLinkedList.add(scanner.nextInt());
        }
        int sum = 0;
        for (int i = 0; i < integerLinkedList.size(); i++) {
            if (integerLinkedList.get(i) % 2 == 0) {
                sum += integerLinkedList.get(i);
            }
        }
        System.out.println("sum is " + sum);
        scanner.close();
    }
}
