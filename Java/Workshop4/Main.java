package Workshop4;

import java.util.LinkedList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        LinkedList<Integer> integerLinkedList = new LinkedList<>();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Input the size of your list: ");
        int n = scanner.nextInt();
        System.out.println("Input the list: ");
        for (int i = 0; i < n; i++) {
            integerLinkedList.add(scanner.nextInt());
        }

        scanner.close();
        System.out.println("peek = " + integerLinkedList.peek());
        System.out.println("list = " + integerLinkedList);
        System.out.println("pop = " + integerLinkedList.pop());
        System.out.println("list = " + integerLinkedList);

        // Добавить в начало списка
        integerLinkedList.addFirst(3);
        System.out.println("list = " + integerLinkedList);
        // Добавить в конец
        integerLinkedList.addLast(7);
        System.out.println("list = " + integerLinkedList);
        // Замена элементов
        integerLinkedList.set(3, 10);
        System.out.println("list = " + integerLinkedList);
        // Проверить на наличие 
        integerLinkedList.contains(3);
        System.out.println("list = " + integerLinkedList);
        // Удаление элемента
        integerLinkedList.remove(3);
        System.out.println("list = " + integerLinkedList);
        integerLinkedList.remove((Integer) 2);
        System.out.println("list = " + integerLinkedList);
    }   
}
