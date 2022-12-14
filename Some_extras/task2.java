package Some_extras;

public class task2 {
    public static void main(String[] args) {
        // byte num; // Просто создали переменную и не добавили в нее значение
        byte num = 23; // От -128 до 127 минимальный тип данных
        
        float num_1 = 23.54f; // обязательно писать f в конце, иначе будет ошибка
        double num_2 = 23.42d; // В два раза больше, чем float. d в конце обязательно
        
        boolean isTrue = true; // 1 - true, 0 - false
        char sym = 'R'; // Один символ, обязательно записывать в одинарных ковычках

        String str = "Hello world!"; // отображает нормально, но бывает нужно импортировать еще один пакет import java.lang.String; Дополнительный класс в котором присутствует данный тип данных

        System.out.print(str);
    }
}
