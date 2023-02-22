public class User implements Comparable<User> {

    private String name;
    private String surname;
    private int age;

    public User(String name, String surname, int age) {
        this.name = name;
        this.surname = surname;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return String.format("Name: %s, Surname: %s, Age: %d", name, surname, age);
    }

    // А теперь реализуем компарэбэл. (Видимо, крайне важная штука)

    @Override
    public int compareTo(User other) {
        int name1 = this.getName().compareTo(other.getName());
        if (name1 != 0) {
            return name1;
        }
        int surname1 = this.getSurname().compareTo(other.getSurname());
        if (surname1 != 0) {
            return surname1;
        }
        
        return this.getAge() - other.getAge(); // отрицательное число - меньше, 0 - равны, положительное - больше 
    
    }


}
