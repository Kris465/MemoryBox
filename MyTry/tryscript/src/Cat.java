public class Cat {
    // Набор полей:
    String name;
    int age;
    String colour;

    // Конструктор. Он как метод, но не имеет типа (void). Имеет тоже имя, что и класс. Его можно перегрузить. У любого класса всегда есть конструктор. Если его не создали, то на уровне байт-кода он создасться по умолчанию (без параметров)
    // public Cat(String name, int age, String colour) {
    //     this.name = name;
    //     this.age = age;
    //     this.colour = colour;
    // }

    // Конструкторы можно программировать самостоятельно. Конструктор по умолчанию:
    public Cat() {

    }

    // Можно создать сколько угодно уникальных конструкторов. У них может быть разное количество сигнатур. Перегрузка методов работает только в том случае, если сигнатуры конструторов уникальны относительно дург друга.(следующие три конструктора вызовут ошибку без пустого конструктора выше)
    public Cat(String newName) {
        name = newName;
        age = 1;
        colour = "Grey";
    }

    public Cat(String newName, int newAge) { //Здесь можем проинициализировать имя - возраст. А цвет задаем по умолчанию.
        name = newName;
        age = newAge;
        colour = "Grey";
    }
    
    public Cat(String newName, int newAge, String newColour) {
        name = newName;
        age = newAge;
        colour = newColour;
    }

    // Метод. ничего не возвращает, но выводит информацию о коте. Характеризует стандартное поведение кота
    void displayInfo() {
        System.out.printf("Name: %s\tAge: %d\tColour: %s", name, age, colour);
    }

}
