public class Toy {
    
    public static int count = 0;
    private int id;
    private String name;
    private int size;
    private String colour;
    
    public Toy(String name, int size, String colour) {
        this.id = Toy.count += 1;
        this.name = name;
        this.size = size;
        this.colour = colour;
    }

    public Toy(Integer id, String name, Integer size, String colour) {
        this.id = id;
        this.name = name;
        this.size = size;
        this.colour = colour;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public String getColour() {
        return colour;
    }

    public void setColour(String colour) {
        this.colour = colour;
    }

    @Override
    public String toString() {
        return String.format("ID: %d, Name: %s, Size: %d, Colour: %s", id, name, size, colour);
    }

}
