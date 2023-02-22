public class View {
    
    private Controller controller;

    public View(Controller controller) {
        this.controller = controller;
    }

    public void run() {
        // тут по идее должна быть какая-то логика отображения команд
        System.out.println(controller.save());
        System.out.println(controller.report());
    }
}
