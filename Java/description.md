# Домашняя работа по шестому семинару по вводному курсу java. 
## Задание:

Подумать над структурой класса Ноутбук для магазина техники - выделить поля и методы. Реализовать в java.

Создать множество ноутбуков.

Написать метод, который будет запрашивать у пользователя критерий (или критерии) фильтрации и выведет ноутбуки, отвечающие фильтру. Критерии фильтрации можно хранить в Map.

Например:

Введите цифру, соответствующую необходимому критерию:

- ОЗУ
- Объем ЖД
- Операционная система
- Цвет

Далее нужно запросить минимальные значения для указанных критериев - сохранить параметры фильтрации можно также в Map.

Отфильтровать ноутбуки их первоначального множества и вывести проходящие по условиям.

## Решение:

Файл **Laptops.java** содержит описанние класса "Ноутбук". В основном файле, который также является и точкой входа, реализован алгоритм сортировки коллекции. 
Сначала мы задаем коллекцию ноутбуков и присваиваем ее в список. Учитывая, что по заданию, нам необоходимо знать минимальные значения для поиска подходящего ноутбука, мы просим у пользователя ввести значения для всех характеристик. В случае, если пользователь введет что-то не то (до тех пор, пока вводимое значение соответствует требуемому типу данных), благодаря операнду **или**, все будет работать. Нам достаточно всего одной совпадающей характеристики, чтобы вывести все подходящие под нее позиции.
# Например: 
1. RAM: 222
2. HDD: 2999
3. OS: jikoladnf
4. Colour: oaidsjfn
5. Size: 16,2

В этом случае все введенные данные соответствуют требуемому типу и сортирока будет по последней характеристике. Программа выведет все ноутбуки, чей размер больше или равен 16.2. 
Таким образом, условие задачи выполненно. Для числовых характеристик мы ищем равное или больше, для строк проверяем совпадение.