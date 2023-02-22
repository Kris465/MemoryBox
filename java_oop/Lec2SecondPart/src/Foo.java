public class Foo {
    public Integer value;

    private static Integer count;
    public static int getCount() {
        return count;// this и super в статике не нужны
    }

    static {
        count = 0;
    }

    public Foo() {
        // count++;
    }

    public void printCount() {
        System.out.println(count);
    }

    @Override
    public String toString() {
        return value.toString();
    }
}
