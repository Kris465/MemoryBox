public class Dish {
    
    private String name;
    private double price;
    private boolean inSale;

    public Dish(String name, double price, boolean inSale) {
        this.name = name;
        this.price = price;
        this.inSale = inSale;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public boolean isInSale() {
        return inSale;
    }

    public void setInSale(boolean inSale) {
        this.inSale = inSale;
    }

    @Override
    public String toString() {
        return "Dish [name=" + name + ", price=" + price + ", inSale=" + inSale + "]";
    }
    
}
