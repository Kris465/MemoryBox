package Extras;

public class task2 {
    public static void main(String[] args) {
        // byte num; // Просто создали переменную и не добавили в нее значение
        byte num = 23; // От -128 до 127 минимальный тип данных
        System.out.println(num);
        
        float num1 = 23.54f; // обязательно писать f в конце, иначе будет ошибка
        double num2 = 23.42d; // В два раза больше, чем float. d в конце обязательно
        System.out.println(num1 + num2);
        
        boolean isTrue = true; // 1 - true, 0 - false
        char sym = 'R'; // Один символ, обязательно записывать в одинарных ковычках
        System.out.println(isTrue);
        System.out.println(sym);

        String str = "Hello world!"; // отображает нормально, но бывает нужно импортировать еще один пакет import java.lang.String; Дополнительный класс в котором присутствует данный тип данных

        System.out.print(str);
    }
}
