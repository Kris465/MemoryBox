package Homework3.Goods;

import java.util.*;

// 1. Дан массив записей: наименование товара, цена, сорт. 
// Найти наибольшую цену товаров 1го или 2го сорта среди товаров, название которых содержит «высший».

public class Main {
    public static void main(String[] args) {
        Goods goods1 = new Goods("Высший Кефир", 1700.0, 2);
        Goods goods2 = new Goods("Молоко",5000.6, 2);
        Goods goods3 = new Goods("Высший Йогурт", 2300.2, 4);
        Goods goods4 = new Goods("Высший Творожок", 1263.2, 3);
        List<Goods> listgoods = new ArrayList<>();
        listgoods.add(goods1);
        listgoods.add(goods2);
        listgoods.add(goods3);
        listgoods.add(goods4);
        double maxVol = 0.0;

        for (int i = 0; i < listgoods.size(); i++) {
            Goods goods = listgoods.get(i);
            if ((goods.getKind() <= 2) && (goods.getName().contains("Высший"))) {
                if (goods.getPrice() > maxVol) {
                    maxVol = goods.getPrice();
                }
            }
        }
        System.out.println("Price is: " + maxVol);
    }
}
