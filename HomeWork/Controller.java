public class Controller implements Action{
    
    private User user;

    public Controller(User user) {
        this.user = user;
    }

    @Override
    public String save(User user) {
        return String.format("Save user: %s", user.getName());
    }

    @Override
    public String report(User user) {
        return String.format("Report for user: %s", user.getName());
    }
}
