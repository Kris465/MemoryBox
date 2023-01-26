public class Cat {
    String name;
    int age;
    String colour;

    
    // Конструктор. Он обычный метод, но не имеет типа void. Его можно перегрузить. У любого класса всегда есть конструктор. Если его не создали, то на уровне байт-кода он создасться по умолчанию (без параметров)
    // public Cat(String name, int age, String colour) {
    //     this.name = name;
    //     this.age = age;
    //     this.colour = colour;
    // }

    public Cat() {

    }

    public Cat() {

    }

    public Cat() {

    }
    
    public Cat() {

    }

    void displayInfo() {
        System.out.printf("Name: %s\tAge: %d\tColour: %s", name, age, colour);
    }

}
