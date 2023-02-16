import java.util.Iterator;

public class Ingredient implements Iterator<String>{
    
    private String name;
    private int amount;

    public Ingredient(String name, int amount) {
        this.name = name;
        this.amount = amount;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    @Override
    public String toString() {
        return String.format("Name: %s, amount: %d", name, amount);
    }

    int index = 0;

    @Override
    public boolean hasNext() {
        return index++ < 2;
    }

    @Override
    public String next() {
        switch (index) {
            case 1: 
                return String.format("Name %s", name);
            case 2: 
                return String.format("amount: %s", amount);
        }
        return name;
    }
}
