public class Cat extends Animal implements Runable {
    
    private String colour;

    public Cat(String name, int box, String colour) {
        super(name, box);
        this.colour = colour;
    }

    @Override
    public String say() {
        return "Meow";
    }

    @Override
    public String toString() {
        return colour + " Cat: " + super.toString();
    }

    @Override
    public int speedOfRun() {
        return 15;
    }
}
