package Homework1;

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
import java.io.FileWriter;
import java.io.IOException;

public class task1 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new FileReader("input.txt"));
        String str;
        String[] in_str;
        double[] a_b = new double[2];
        int numbers;
        int i = 0;
        while ((str = br.readLine()) != null) {           
            in_str = str.split("\\D+");
            numbers = Integer.parseInt(String.join("", in_str));
            a_b[i] = numbers;
            i++;
        }
        br.close();
        
        double multi = Math.pow(a_b[0], a_b[1]);
        int output_str = (int) multi;

        System.out.print(multi);

        try (FileWriter fw = new FileWriter("output.txt", true)) {   
            fw.write(Integer.toString(output_str));
            fw.flush();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
    }
}
