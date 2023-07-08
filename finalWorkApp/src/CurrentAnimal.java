public class CurrentAnimal extends Animal implements Action, AnimalType {
    private String type;
    private int id;

    public CurrentAnimal(String name, int age, String type, int id) {
        super(name, age);
        this.type = type;
        this.id = id;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    @Override
    public void performAction() {
        // TODO Auto-generated method stub
        
    }

    @Override
    public void perform() {
        // TODO Auto-generated method stub
        
    }
}
