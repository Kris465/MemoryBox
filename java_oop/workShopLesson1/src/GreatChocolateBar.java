public class GreatChocolateBar extends ChocolateBar {
    
    private TypeSize size;

    public GreatChocolateBar(double cost, String name, double calories, TypeSize size) {
        super(cost, name, calories);
        this.size = size;
    }

    @Override
    public String toString() {
        return super.toString() + size;
    }
}
