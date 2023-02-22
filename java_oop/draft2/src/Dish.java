
public class Dish {
    
    Ingredient name;
    private Dish nextDishName;
    private Dish lastDishName;
    
    public Dish(Ingredient name) {
        this.name = name;
    }

    public Ingredient getName() {
        return name;
    }

    public void setName(Ingredient name) {
        this.name = name;
    }

    public Dish getNextDishName() {
        return nextDishName;
    }

    public void setNextDishName(Dish nextDishName) {
        this.nextDishName = nextDishName;
    }

    public Dish getLastDishName() {
        return lastDishName;
    }

    public void setLastDishName(Dish lastDishName) {
        this.lastDishName = lastDishName;
    }
}
