package Homework6;

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
import java.util.List;
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
        
        System.out.println("Input the number of your wished option: \n 1.RAM \n 2.HDD \n 3.OS \n 4.Colour \n 5.Size");
        Scanner scanner = new Scanner(System.in);
        
    }
}
