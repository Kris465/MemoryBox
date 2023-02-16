import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Table implements Iterator{
    
    private List userChoice = new ArrayList<>();

    public Table(List userChoice) {
        this.userChoice = userChoice;
    }

    public List getUserChoice() {
        return userChoice;
    }

    public void addUserChoice(Object object) {
        userChoice.add(object);
    }

    int index = 0;

    @Override
    public boolean hasNext() {
        return index < userChoice.size();
    }

    @Override
    public Object next() {
        return userChoice.get(index++);
    }
}
