import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Controller {
    
    private final Action action;

    public Controller(Action action) {
        this.action = action;
    }

    public Lottery createLottery(Lottery lottery) {
        ArrayList<String> colours = new ArrayList<>(List.of("blue", "green", "yellow", "oringe"));
        ArrayList<String> names = new ArrayList<>(List.of("Doll", "Boll", "Car", "puzzles"));

        Random random = new Random();

        for(int i = 0; i < 100; i++){
            lottery.getToysList().add(new Toy(i+ 1, names.get(random.nextInt(names.size())), random.nextInt(10), colours.get(random.nextInt(colours.size()))));
        }

        return lottery;
    }

    public Toy showPrize(Lottery lottery) {

        Random random = new Random();
        Toy prize = lottery.getToysList().get(random.nextInt(lottery.getToysList().size()));
        action.addPrize(prize);
        return prize;

    }

    public List<Toy> showAll() {
        return action.getAllPrizes();
    }

    public void addToys(Lottery lottery) {
        
    }
}
