import java.util.List;

public class Controller {
    
    public void createAnimal(String name) {
        CurrentAnimal animal = new CurrentAnimal(name);
        mapper.saveToFile(animal, "animals.txt");
    }

    public void showAnimalList() {
        List<CurrentAnimal> animals = mapper.readFromFile("animals.txt");
        for (CurrentAnimal animal : animals) {
            System.out.println(animal.getName());
        }
    }

    public void showAnimalSkills() {
    }

    public void trainAnimal(String name, String skill) {
    }
}
