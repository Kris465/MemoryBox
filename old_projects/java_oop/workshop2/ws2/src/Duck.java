public class Duck extends Animal implements Runable, Flyable, Swimable{

    public Duck(String name, int box) {
        super(name, box);
    }

    @Override
    public String say() {
        return "quack quack";
    }

    @Override
    public int speedOfRun() {
        return 10;
    }

    @Override
    public int speedOfFly() {
        return 40;
    }

    @Override
    public int speedOfSwim() {
        return 30;
    }
}
