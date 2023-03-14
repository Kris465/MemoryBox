import java.util.List;
import java.util.Scanner;

public class View {
    
    private Controller controller;

    public View(Controller controller) {
        this.controller = controller;
    }

    public void run() {
        Commands com = Commands.NONE;
    
    while (true) {
        String command = prompt("Input you command: ").toUpperCase();
        com = Commands.valueOf(command);
        if (com == Commands.EXIT) return;
        Lottery lottery = new Lottery();
        controller.addToys(lottery, 30);
        switch (com) {
            case ADD:
                int size = Integer.valueOf(prompt("How many toys?"));
                controller.addToys(lottery, size);
                for(Toy toy : lottery.getToysList()) {
                    System.out.println(toy);
                }
                break;
            case LOTTERY:
                Toy prize = controller.showPrize(lottery);
                System.out.println(prize);
                break;
            case PRIZES:
                controller.showAll().forEach(System.out::println);
                break;
            }
        }
    }

    private String prompt(String message) {
        Scanner in = new Scanner(System.in);
        System.out.print(message);
        return in.nextLine();
    }
}
