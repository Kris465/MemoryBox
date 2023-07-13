public class Animal {
    private int id;
    private String name;
    private String type;
    private int age;
    private String skills = "";
    
    public Animal(int id, String name, String type, int age, String skills) {
        this(id, name, type, age);
        this.skills = skills;
    }

    public Animal(int id, String name, String type, int age) {
        this.id = id;
        this.name = name;
        this.type = type;
        this.age = age;
    }

    public Animal() {
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

    public String getSkills() {
        return skills;
    }

    public void setSkills(String skills) {
        StringBuilder stringBuilder = new StringBuilder(this.skills);
        stringBuilder.append(skills);
        this.skills = new String(stringBuilder);
    }

    @Override
    public String toString() {
        return String.format("ID: %d, Name: %s, age: %d, type: %s, skills: %s", id, name, age, type, skills);
    }
}
