import java.util.List;

public interface Action {
    
    List<Toy> getAllPrizes();
    void addPrize(Toy toy);
    void saveAllLines(List<Toy> toys);
}
