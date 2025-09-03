public class Dish {
    
    private String name;
    private Ingredient ingredients;
    private int price;
    
    public Dish(String name, Ingredient ingredients, int price) {
        this.name = name;
        this.ingredients = ingredients;
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Ingredient getIngredients() {
        return ingredients;
    }

    public void setIngredients(Ingredient ingredients) {
        this.ingredients = ingredients;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    @Override
    public String toString() {
        return "Dish [name=" + name + ", ingredients=" + ingredients + ", price=" + price + "]";
    }

}
