import java.util.ArrayList;
import java.util.List;

public class Lottery {
    
    private List<Toy> toysList;

    public Lottery(List<Toy> toysList) {
        this.toysList = new ArrayList<Toy>();
    }

    public List<Toy> getToysList() {
        return toysList;
    }

    public void setToysList(List<Toy> toysList) {
        this.toysList = toysList;
    }
}
