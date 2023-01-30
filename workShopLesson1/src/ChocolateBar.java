public class ChocolateBar extends Product {
    
    private double calories;

    public ChocolateBar(double cost, String name, double calories) {
        super(cost, "Mars");
        this.calories = calories;
    }

    public double getCalories() {
        return calories;
    }

    @Override
    public String toString() {
        return super.toString() + "(calories: " + this.calories + ")"; //бегает к другому переопределению
    }

}
