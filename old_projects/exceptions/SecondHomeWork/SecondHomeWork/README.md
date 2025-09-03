# Домашняя работа 2

## Задание 1. 
    Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float), и возвращает введенное значение. Ввод текста вместо числа не должно приводить к падению приложения, вместо этого, необходимо повторно запросить у пользователя ввод данных.

Классы, работающие с ошибками при вводе текста:

- InputMismatchException - исключение, которое возникает при попытке считать данные из Scanner, которые не соответствуют ожидаемому типу данных.
- NumberFormatException - исключение, которое возникает при попытке преобразовать строку в числовой тип, если строка не содержит корректного числа.
- Также в конце можно использовать базовый класс исключение. Java идет до первого подходящего исключения, поэтому узкие (специальные) исключения в начале, общее исключение - в конце.

## Задание 2.
    Если необходимо, исправьте данный код (https://docs.google.com/document/d/17EaA1lDxzD5YigQ5OAal60fOFKVoCbEJqooB9XfhT7w/edit)

```java
try {
   int d = 0;
   double catchedRes1 = intArray[8] / d;
   System.out.println("catchedRes1 = " + catchedRes1);
} catch (ArithmeticException e) {
   System.out.println("Catching exception: " + e);
}
```
С точки зрения синтаксиса код верен, поэтому его можно не исправить, а улучшить:

```java
public static void processArray() {
   Scanner scanner = new Scanner(System.in);
   int[] intArray = new int[10];
   int d = 0;
   try {
      System.out.println("Введите 10 чисел, отделяя их друг от друга пробелами: ");
      for (int i = 0; i < 10; i++) {
         intArray[i] = scanner.nextInt();
      }
      System.out.println("Введите число d, но помните, что на ноль делить нельзя: ");
      d = scanner.nextInt();
      double catchedRes1 = intArray[8] / (double)d;
      System.out.println("Результат: " + catchedRes1);
   } catch (ArithmeticException e) {
      System.out.println("А я предупреждал... " + e);
   } catch (ArrayIndexOutOfBoundsException e) {
      System.out.println("Просил же 10 чисел... " + e);
   } catch (InputMismatchException e) {
      System.out.println("Числа, мать, числа! " + e);
   }
}
```

## Задание 3.
    Дан следующий код, исправьте его там, где требуется (https://docs.google.com/document/d/17EaA1lDxzD5YigQ5OAal60fOFKVoCbEJqooB9XfhT7w/edit)

```java
public static void main(String[] args) throws Exception {
   try {
       int a = 90;
       int b = 3;
       System.out.println(a / b);
       printSum(23, 234);
       int[] abc = { 1, 2 };
       abc[3] = 9;
   } catch (Throwable ex) {
       System.out.println("Что-то пошло не так...");
   } catch (NullPointerException ex) {
       System.out.println("Указатель не может указывать на null!");
   } catch (IndexOutOfBoundsException ex) {
       System.out.println("Массив выходит за пределы своего размера!");
   }
}
public static void printSum(Integer a, Integer b) throws FileNotFoundException {
   System.out.println(a + b);
}
```
1. Очевидно, логика метода должна оставаться внутри метода. Поэтому обработку ошибок переносим из main() в operations() (переименованный printSum). 
2. Множество разнообразных действий мы собираем в один алгоритм. 
Если же нам нужен калькулятор, то каждое действие должно быть разнесено по плогике в отдельные методы с собственными обработками ошибок.
3. (Throwable ex) меняем на (Exception ex) и помещаем в конце алгоритма, потому что это максимально общая ошибка. (Throwable ex) может обрабатывать ошибки виртуальной машины, это излишество, если мы понимаем, что работаем только со вводом и вычислениями.
4. Присвоение в третий индекс массива - бред, потому что нарушена логика программы. Магических чисел в коде быть не должно, поэтому заменяем на простое добавление в массив. Следовательно, и допольнительной обработки этой ошибки не нужно. Так или иначе в конце добавлена общая ошибка, если что-то пойдет не так, она обеспечит стабильность программы.


```java
public void operations() {
    Scanner scanner = new Scanner(System.in);
    List<Integer> numbers = new ArrayList<>();
    try {
        System.out.print("Введите первое число: ");
        int num1 = scanner.nextInt();
        System.out.print("Введите второе число: ");
        int num2 = scanner.nextInt();
        numbers.add(num1);
        numbers.add(num2);
        int result = num1 / num2;
        System.out.println("Результат деления: " + result);
        numbers.add(result);
        int sum = num1 + num2;
        System.out.println("Сумма чисел: " + sum);
        numbers.add(sum);
    } catch (InputMismatchException ex) {
        System.out.println("Неверный формат ввода!");
    } catch (ArithmeticException ex) {
        System.out.println("Деление на ноль!");
    } catch (Exception ex) {
        System.out.println("Произошла ошибка: " + ex.getMessage());
    }
}
```

## Задание 4.
    Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку. Пользователю должно показаться сообщение, что пустые строки вводить нельзя

Метод trim() обрезает лишние пробелы вначале и конце строки. Поэтому если строка состоит только из них, этот метод удалит все. А дальше обработка ошибки.
