package Homework4;

import java.util.LinkedList;
import java.util.Scanner;

//Определить является ли список знакочередующимся? (без массивов)

public class task2 {
    public static void main(String[] args) {
        LinkedList<Integer> integerLinkedList = new LinkedList<>();
        System.out.println("Input the size of your list: ");
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println("Input the values of your list: ");
        Boolean askedFlag = false;
        for (int i = 0; i < n; i++) {
            integerLinkedList.add(scanner.nextInt());
        }
        scanner.close();    
        
        int a = integerLinkedList.get(0);
        int b = integerLinkedList.get(1);
        int k = 2;
        while (k < (n - 1)) {
            if ((a > 0 && b < 0) || (a < 0 && b > 0)) {
                a = integerLinkedList.get(k);
                b = integerLinkedList.get(k + 1);
                askedFlag = true;
                k += 2;
            } else {
                askedFlag = false;
                break;
            }
        } 
        if (askedFlag == true) {
            System.out.println("Yes, it is.");
        } else {
            System.out.println("No, it isn't");
        }
    }
}
