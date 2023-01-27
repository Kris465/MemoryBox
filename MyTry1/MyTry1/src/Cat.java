public class Cat {
    
    String name;
    int age;
    String colour;

    public Cat(String name, int age, String colour) {
        this.name = name;
        this.age = age;
        this.colour = colour;
    }

    public Cat(String name, int age) {
        this(name, age, "Grey");
    }

    public Cat(String name) {
        this(name, 4, "White");
    }

    void displayInfo() {
        System.out.printf("Name: %s\tAge: %d\tColour: %s\n", name, age, colour);
    }
}
