public class FinDirector{
    private String name;
    private int age;
    private Counter counter;
    
    public FinDirector(String name, int age, Counter counter) {
        this.name = name;
        this.age = age;
        this.counter = counter;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public Counter getCounter() {
        return counter;
    }

    @Override
    public String toString() {
        return "FinDirector [name=" + name + ", age=" + age + ", counter=" + counter + "]";
    }
}
