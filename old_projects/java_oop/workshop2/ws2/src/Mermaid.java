public class Mermaid extends Animal implements Swimable{

    public Mermaid(String name, int box) {
        super(name, box);
    }

    @Override
    public String say() {
        return "Singing";
    }

    @Override
    public int speedOfSwim() {
        return 50;
    }
}
