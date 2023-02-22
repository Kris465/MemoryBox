public class Cat {
    
    String name;
    int age;
    String colour;

    public Cat(String name, int age, String colour) {

        if (age > 0) 
            this.age = age;
        else
            this.age = 1; //Защищаем поле age от отрицательного возрастра

        this.name = name;
        this.colour = colour;
    }

    public Cat(String name, int age) {
        this(name, age, "Grey");
    }

    public Cat(String name) {
        this(name, 4);
    }

    void displayInfo() {
        System.out.printf("Name: %s\tAge: %d\tColour: %s\n", name, age, colour);
    }
}
