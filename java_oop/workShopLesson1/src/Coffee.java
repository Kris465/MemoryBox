public class Coffee extends Product{
    
    private boolean milk;

    public Coffee(double cost, String name, boolean milk) {
        super(cost, name);
        this.milk = milk;
    }

    public boolean getMilk() {
        return milk;
    }

    @Override
    public String toString() {
        return super.toString() + " Milk: " + milk;
    }
}
