package Workshop3;

import java.util.*;

import Workshop3.Goods.*;

public class Main {
    public static void main(String[] args) {
        Goods goods1 = new Goods("qwe2", "rt1", 5);
        Goods goods2 = new Goods("qwe", "rt2", 6);
        Goods goods3 = new Goods("qwe2", "rt14", 7);
        List<Goods> listGoods = new ArrayList<>();
        listGoods.add(goods1);
        listGoods.add(goods2);
        listGoods.add(goods3);
        String search="qwe2";
        Integer totalExportVolume = 0;
        Set<String> setCountry = new HashSet<>();
        for (int i = 0; i < listGoods.size(); i++) {
            if(listGoods.get(i).getName().equals(search)) {
                setCountry.add(listGoods.get(i).getCountry());
                totalExportVolume += listGoods.get(i).getVolume();
            }
        }
        System.out.println("setCountry = " + setCountry);
        System.out.println("totalExportVolume = " + totalExportVolume);
    }
}
