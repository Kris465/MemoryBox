package Homework5;

import java.util.HashMap;
import java.util.Map;

// 1) Подсчитать количество вхождения каждого слова
// Пример:
// Россия идет вперед всей планеты. Планета — это не Россия.
// toLoverCase().

public class task1 {
    public static void main(String[] args) {
        Map<String, Integer> map = new HashMap<>();
        String str = "Russia goes ahead of the whole planet. The planet is not Russia.";
        str = str.toLowerCase();
        str = str.replace(".", "");
        String[] words = str.split(" ");
        for (int i = 0; i < words.length; i++) {
            if (map.containsKey(words[i])) {
                map.put(words[i], map.get(words[i]) + 1);
            } else {
                map.put(words[i], 1);
            }
        }
        for (Map.Entry<String, Integer> entry :map.entrySet()) {
            System.out.println("The word - " + entry.getKey() + " - meets " + entry.getValue());
        }
    }
}
