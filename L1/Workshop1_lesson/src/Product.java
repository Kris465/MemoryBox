public class Product {
    
    private double cost;
    private String name;

    public Product(double cost, String name) {
        this.cost = cost;
        this.name = name;
    }

    /**
     * @return the cost
     */
    public double getCost() {
        return cost;
    }

    /**
     * @return the name
     */
    public String getName() {
        return name;
    }

    
}
