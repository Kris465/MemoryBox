import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Table implements Iterable<Dish> {
    
    private List<Dish> dishes = new ArrayList<>();

    public void addDish(Dish dish) {
        dishes.add(dish);
    }

    @Override
    public Iterator<Dish> iterator() {
        return new Iterator<Dish>(){

            private int currentIndex = 0;

            @Override
            public boolean hasNext() {
                
                return false;
            }

            @Override
            public Dish next() {
                return null;
            }
            
        };
    }
}
