public class App {
    public static void main(String[] args) throws Exception {
        FileOperation fileOperation = new FileOperationImpl("notes.txt");
        Action action = new ActionFile(fileOperation);
        Controller controller = new Controller(action);
        View view = new View(controller);
        view.run();
    }
}
