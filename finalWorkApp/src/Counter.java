public class Counter {
    private int count;

    public Counter() {
        count = 0;
    }

    public int getNextId() {
        return ++count;
    }
}
