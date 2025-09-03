import java.util.Iterator;

public class Counter implements Iterator<String> {
    private String name;
    private int age;
    private int salary;

    public Counter(String name, int age, int salary) {

        this.name = name;
        this.age = age;
        this.salary = salary;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public int getSalary() {
        return salary;
    }

    @Override
    public String toString() {
        return "Counter [name=" + name + ", age=" + age + ", salary=" + salary + "]";
    }

    int index;

    @Override
    public boolean hasNext() {

        return index++ < 3;
    }

    @Override
    public String next() {
        switch (index) {
            case 1:
                return String.format("Name: %s", name);
            case 2:
                return String.format("Age: %d", age);
            case 3:
                return String.format("Salary: %d", salary);
        }
        return name;

    }

}
