package Homework5;

import java.util.HashMap;
import java.util.Map;

// 3) Найти пересечения слов в массивах и указать их общее количество.
// Пример:
// mas1= [“qwe”,”asd”,”qwe”,”x”]
// mas2=[“qwe”,”v”]
// Результат:
// qwe=3

public class task3 {
    public static void main(String[] args) {
        String[] mas1 = new String[]{"qwe", "asd", "qwe", "x", "r"};
        String[] mas2 = new String[]{"qwe", "v", "r"};
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < mas1.length; i++) {
            if (map.containsKey(mas1[i])) {
                map.put(mas1[i], map.get(mas1[i]) + 1);
            } else {
                map.put(mas1[i], 1);
            }
        }
        for (int k = 0; k < mas2.length; k++) {
            if (map.containsKey(mas2[k])) {
                map.put(mas2[k], map.get(mas2[k]) + 1);
            } else {
                map.put(mas2[k], 1);
            }
        }
        for (Map.Entry<String, Integer> entry :map.entrySet()) {
            if (entry.getValue() > 1) {
                System.out.println(entry.getKey() + " = " + entry.getValue());
            }
        }
    }
}
