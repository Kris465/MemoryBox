public class Horse extends Animal implements Runable{

    public Horse(String name, int box) {
        super(name, box);
    }

    @Override
    public String say() {
        return "Yoke";
    }

    @Override
    public String toString() {
        return "Horse: " + super.toString();
    }

    @Override
    public int speedOfRun() {
        return 60;
    }
}
