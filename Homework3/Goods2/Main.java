package Homework3.Goods2;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// 2. Сведения о товаре состоят из наименования, страны-производителя, веса, цены, сорта. 
// Получить наименования товаров заданного сорта с наименьшей ценой.

public class Main {
    public static void main(String[] args) {
        Goods2 goods1 = new Goods2("Кефир", "Россия", 1000, 100.0, 2);
        Goods2 goods2 = new Goods2("Молоко", "Финляндия", 1800, 135.6, 2);
        Goods2 goods3 = new Goods2("Йогурт", "Америка", 120, 63.2, 2);
        Goods2 goods4 = new Goods2("Творожок", "Аргентина", 80, 63.2, 2);
        List<Goods2> listgoods = new ArrayList<>();
        listgoods.add(goods1);
        listgoods.add(goods2);
        listgoods.add(goods3);
        listgoods.add(goods4);

        System.out.println("Input the number of kind: ");
        Scanner scanner = new Scanner(System.in);
        Integer userKind = scanner.nextInt();
        double minVol = goods1.getPrice();
        scanner.close();

        for (int i = 0; i < listgoods.size(); i++) {
            Goods2 goods = listgoods.get(i);
            if (goods.getKind() == userKind) {
                if (goods.getPrice() < minVol) {
                    minVol = goods.getPrice();                  
                }
            } else {
                minVol = -1;
            }
        }

        for (int i = 0; i < listgoods.size(); i++) {
            Goods2 goods = listgoods.get(i);
            if (goods.getPrice() == minVol) {
                System.out.print(goods.getName() + " ");
            }
        }
    }
}
