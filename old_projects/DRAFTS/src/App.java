import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class App {
    public static void main(String[] args) {
        
        Lottery lottery = new Lottery(null);

        ArrayList<String> colours = new ArrayList<>(List.of("blue", "green", "yellow", "oringe"));
        ArrayList<String> names = new ArrayList<>(List.of("Doll", "Boll", "Car", "puzzles"));

        Random random = new Random();

        for(int i = 0; i < 100; i++){
            lottery.getToysList().add(new Toy(i+ 1, names.get(random.nextInt(names.size())), random.nextInt(10), colours.get(random.nextInt(colours.size()))));
        }

        for(Toy toy : lottery.getToysList()) {
            System.out.println(toy);
        }

        System.out.println(lottery.getToysList().get(random.nextInt(lottery.getToysList().size())));
    }
}
