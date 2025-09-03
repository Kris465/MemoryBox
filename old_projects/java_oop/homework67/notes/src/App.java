public class App {
    public static void main(String[] args) {
        FileOperation fileOperation = new FileOperationImp("notes.txt");
        Repository repository = new RepositoryFile(fileOperation);
        Controller controller = new Controller(repository);
        View view = new View(controller);
        view.run();
    }
}
