public class App {
    public static void main(String[] args){
        
        FileOperation fileOperation = new FileOperationImp("prizes.txt");
        Action action = new ActionFile(fileOperation);
        Controller controller = new Controller(action);
        View view = new View(controller);
        view.run();

    }
}
