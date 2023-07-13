import java.util.ArrayList;
import java.util.List;

public class Controller {
    private FileOperation fileOperation;
    
    public Controller(FileOperation fileOperation) {
        this.fileOperation = fileOperation;
    }
    
    public List<Animal> getAllAnimals() {
        return fileOperation.readFromFile("animals.txt");
    }
    
    public List<String> getAllAnimalsInfo() {
        List<Animal> animals = fileOperation.readFromFile("animals.txt");
        List<String> animalInfo = new ArrayList<>();
        
        for (Animal animal : animals) {
            animalInfo.add(animal.getId() + ", " + animal.getName());
        }
        
        return animalInfo;
    }
    
    public Animal findAnimalById(int id) {
        List<Animal> animals = fileOperation.readFromFile("animals.txt");
        
        for (Animal animal : animals) {
            if (animal.getId() == id) {
                return animal;
            }
        }
        
        return null;
    }
    
    public void changeAnimalType(int id, String newType) {
        List<Animal> animals = fileOperation.readFromFile("animals.txt");
        
        for (Animal animal : animals) {
            if (animal.getId() == id) {
                animal.setType(newType);
                break;
            }
        }
        
        fileOperation.writeToFile(animals, "animals.txt");
    }
    
    public void teachAnimalCommand(int id, String command) {
        List<Animal> animals = fileOperation.readFromFile("animals.txt");
        
        for (Animal animal : animals) {
            if (animal.getId() == id) {
                animal.setSkills(command);
                break;
            }
        }
        
        fileOperation.writeToFile(animals, "animals.txt");
    }

    public void addAnimal(Animal newAnimal) {
        List<Animal> animals = getAllAnimals();

        animals.add(newAnimal);
        fileOperation.writeToFile(animals, "animals.txt");
    }
}
