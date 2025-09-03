import java.util.Iterator;

public class Table implements Iterable {
    
    private Dish headName;
    private Dish tailName;
    private int count = 0;

    @Override
    public Iterator iterator() {
        return new Iterator<Ingredient>() {
            Dish dish = new Dish("salad");
            {
                dish.setNextDishName(headName);
            }
            Dish currentDish = dish;
            
            @Override
            public boolean hasNext() {
                return currentDish.getNextDishName() != null;
            }
            @Override
            public Ingredient next() {
                currentDish = currentDish.getNextDishName();
                return currentDish.getName();
            }
        };
    }

    public int size() {
        return count;
    }

    private Dish getIngredient(int index) {
        if (index >= count) {
            throw new IndexOutOfBoundsException();
        }

        Ingredient result = headDish;
        for (int i 1;)
    }


}
