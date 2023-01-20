package Extras;
import java.util.Scanner; // специальный класс, позволяющий нам сканировать или брать данные от пользователя

public class task3 {
    public static void main(String[] args) {
        Scanner str = new Scanner(System.in); // str - переменная объекта Scanner, в которую мы присваиваем значение функции Scanner(Берем System и делаем в нее in)
        System.out.println("Your string is: " + str.nextLine()); // для вывода int можем использовать ...nextInt()
        // Через + я сложила несколько строк в выводе
        str.close();
    }
}
