public class Director {
    private String name;
    private int age;
    private FinDirector finDirector;
   


    public Director(String name, int age, FinDirector finDirector) {
        this.name = name;
        this.age = age;
        this.finDirector = finDirector;
    }


    public String getName() {
        return name;
    }



    public int getAge() {
        return age;
    }



    public FinDirector getFinDirector() {
        return finDirector;
    }


    @Override
    public String toString() {
        return "Director [name=" + name + ", age=" + age + ", finDirector=" + finDirector + "]";
    }


}
