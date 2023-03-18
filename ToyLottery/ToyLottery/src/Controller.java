import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Controller {
    
    private final Action action;

    public Controller(Action action) {
        this.action = action;
    }

    public Lottery generate(Lottery lottery, int size) {
        ArrayList<String> colours = new ArrayList<>(List.of("blue", "green", "yellow", "oringe"));
        ArrayList<String> names = new ArrayList<>(List.of("Doll", "Boll", "Car", "puzzles"));

        Random random = new Random();

        for(int i = 0; i < size; i++){
            lottery.getToysList().add(new Toy(names.get(random.nextInt(names.size())), random.nextInt(10), colours.get(random.nextInt(colours.size()))));
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

    public Lottery addToys(Lottery lottery, int size) {
        return generate(lottery, size);
    }
}
