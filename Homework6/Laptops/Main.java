package Homework6.Laptops;

// Задание:
// • Подумать над структурой класса Ноутбук для магазина техники - выделить поля и методы. Реализовать в java.
// • Создать множество ноутбуков.
// • Написать метод, который будет запрашивать у пользователя критерий (или критерии) фильтрации и выведет ноутбуки, отвечающие фильтру. Критерии фильтрации можно хранить в Map. Например:
// “Введите цифру, соответствующую необходимому критерию:
// 1 - ОЗУ
// 2 - Объем ЖД
// 3 - Операционная система
// 4 - Цвет …
// • Далее нужно запросить минимальные значения для указанных критериев - сохранить параметры фильтрации можно также в Map.
// • Отфильтровать ноутбуки их первоначального множества и вывести проходящие по условиям.

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Laptops laptop1 = new Laptops(2, 200, "Windows", "black", 19.2);
        Laptops laptop2 = new Laptops(4, 100, "Mac", "blue", 14.2);
        Laptops laptop3 = new Laptops(2, 500, "Linux", "red", 20.3);
        Laptops laptop4 = new Laptops(8, 100, "Windows", "green", 16.2);
        List<Laptops> listLaptops = new ArrayList<>();
        listLaptops.add(laptop1);
        listLaptops.add(laptop2);
        listLaptops.add(laptop3);
        listLaptops.add(laptop4);
        
        Scanner scanner = new Scanner(System.in);
        Map<Integer, String> map = new HashMap<>();
        
        System.out.println("Input you wished values. 1. RAM: ");
        map.put(1, scanner.nextLine());
        System.out.println("2. HDD: ");
        map.put(2, scanner.nextLine());
        System.out.println("3. OS: ");
        map.put(3, scanner.nextLine());
        System.out.println("4. Colour: ");
        map.put(4, scanner.nextLine());
        System.out.println("5. Size: ");
        map.put(5, scanner.nextLine());
        
        for (Map.Entry<Integer, String> entry :map.entrySet()) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }

        List<Laptops> outputLaptops = new ArrayList<>();

        int option = 5;
        switch (option) {
            case 1:
                var tempValue = map.get(1);
                if (listLaptops.contains(tempValue)) {
                    int index = listLaptops.indexOf(tempValue);
                    outputLaptops.add(listLaptops.get(index)); 
                }
        }


        scanner.close();
    }

    
}
