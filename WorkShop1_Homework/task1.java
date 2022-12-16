package WorkShop1_Homework;

// +Реализовать функцию возведения числа а в степень b. a, b ∈ Z. Сводя количество выполняемых действий к минимуму.
// Пример 1: а = 3, b = 2, ответ: 9
// Пример 2: а = 2, b = -2, ответ: 0.25
// Пример 3: а = 3, b = 0, ответ: 1
// Пример 4: а = 0, b = 0, ответ: не определено
// Пример 5
// входные данные находятся в файле input.txt в виде
// b 3
// a 10
// Результат нужно сохранить в файле output.txt
// 1000

import java.io.*;
import java.lang.String;
import java.utils.Arrays;

public class task1 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new FileReader("input.txt"));
        String str;
        String[] in_str;
        int[] a_b = new int[2];
        int numbers;
        int a;
        int b;
        while ((str = br.readLine()) != null) {           
            in_str = str.split("\\D+");
            numbers = Integer.parseInt(String.join("", in_str));
            
            
            System.out.println(numbers);
        }
        br.close();
    }
}
