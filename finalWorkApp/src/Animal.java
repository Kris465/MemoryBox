import java.util.List;

public class Animal {
    private int id;
    private String name;
    private String type;
    private int age;
    private List<String> skills;
    
    public Animal(int id, String name, String type, int age, List<String> skills) {
        this.id = id;
        this.name = name;
        this.type = type;
        this.age = age;
        this.skills = skills;
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

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public List<String> getSkills() {
        return skills;
    }

    public void setSkills(List<String> skills) {
        this.skills = skills;
    }

    @Override
    public String toString() {
        return String.format("ID: %d, Name: %s, age: %d, type: %s", id, name, age, type);
    }

}
