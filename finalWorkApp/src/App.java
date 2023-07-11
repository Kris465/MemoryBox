public class App {
    public static void main(String[] args) {
        FileOperation FileOperation = new FileOperation();
        Controller controller = new Controller(FileOperation);
        Counter counter = new Counter("animals.txt");
        View view = new View(controller, counter);
        view.start();
    }
}
