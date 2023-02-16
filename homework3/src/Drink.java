public class Drink {
    
    private String name;
    private Ingredient ingredients;
    private int size;
    
    public Drink(String name, Ingredient ingredients, int size) {
        this.name = name;
        this.ingredients = ingredients;
        this.size = size;
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

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    @Override
    public String toString() {
        return String.format("Drink: %s, Contains: %s, size: %d", name, ingredients, size);
    }
}
