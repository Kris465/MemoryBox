public class ViewUser {
    
    private Controller controller;

    public ViewUser(Controller controller) {
        this.controller = controller;
    }

    public void run() {
        controller.save();
    }

    
    
}
