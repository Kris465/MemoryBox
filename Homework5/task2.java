package Homework5;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

// 2) Подсчитать количество искомого слова, через map (наполнением значение, где искомое слово будет являться ключом)

public class task2 {
    public static void main(String[] args) {
        Map<String, Integer> map = new HashMap<>();
        String str = "Russia goes ahead of the whole planet. The planet is not Russia.";
        str = str.toLowerCase();
        str = str.replace(".", "");
        String[] words = str.split(" ");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Input your word: ");
        String userWord = scanner.nextLine();
        userWord = userWord.toLowerCase();
        map.put(userWord, 0);
        scanner.close();

        for (int i = 0; i < words.length; i++) {
            if (words[i].equals(userWord)) {
                map.put(userWord, map.get(userWord) + 1);
            }
        }
        for (Map.Entry<String, Integer> entry :map.entrySet()) {
            System.out.println("Your word - " + entry.getKey() + " - meets " + entry.getValue());
        }
    }
}
