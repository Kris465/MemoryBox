public class App {

    public static void main(String[] args) {
        
        Cat cat01 = new Cat("Peach", 8, "red");
        cat01.displayInfo();

        Cat cat02 = new Cat("Fluffy", 6);
        cat02.displayInfo();

        Cat cat03 = new Cat("Tiger");
        cat03.displayInfo();

        cat03.colour = "Black";
        cat03.displayInfo();
    }
}
