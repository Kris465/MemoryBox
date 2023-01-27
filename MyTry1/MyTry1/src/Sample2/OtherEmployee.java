package Sample2;

public class OtherEmployee {
    
    private String name;
    private int age;
    private String work;
    
    public int getAge() { // Возвращает значение поля - акцессор
        return age;
    }

    public void setAge(int age) { // Задает значение поля - мутатор
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getWork() {
        return work;
    }

    public void setWork(String work) {
        this.work = work;
    }

}
