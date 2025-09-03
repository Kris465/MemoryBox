public class Product {
    
    private double cost;
    private String name;

    public Product(double cost, String name) {
        this.cost = cost;
        this.name = name;
    }

    public double getCost() {
        return cost;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return "Product cost = " + cost + ", name = " + name;
    }
}
