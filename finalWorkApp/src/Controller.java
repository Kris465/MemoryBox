import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Controller {
    private List<Animal> animals;
    
    public Controller() {
        animals = new ArrayList<>();
    }
    
    public void addAnimal() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the animal's name: ");
        String name = scanner.nextLine();
        System.out.println("Enter the animal's type: ");
        String type = scanner.nextLine();
        
        Animal animal = new Animal(0, name, type, 0, null);
        animals.add(animal);
        
        saveAnimalsToFile();
    }
    
    public void showAllAnimals() {
        readAnimalsFromFile();
        
        for (Animal animal : animals) {
            System.out.println("Name: " + animal.getName());
            System.out.println("Type: " + animal.getType());
            System.out.println("Skills: " + animal.getSkills());
            System.out.println();
        }
    }
    
    public Animal getAnimalByName(String name) {
        readAnimalsFromFile();
        
        for (Animal animal : animals) {
            if (animal.getName().equals(name)) {
                return animal;
            }
        }
        
        return null;
    }
    
    private void saveAnimalsToFile() {
        try (PrintWriter writer = new PrintWriter(new FileWriter("animals.txt"))) {
            for (Animal animal : animals) {
                writer.println(animal.getName() + "," + animal.getType() + "," + animal.getSkills());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    private void readAnimalsFromFile() {
        animals.clear();
        
        try (Scanner scanner = new Scanner(new File("animals.txt"))) {
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] parts = line.split(",");
                String name = parts[0];
                String type = parts[1];
                List<String> skills = Arrays.asList(parts[2].split(";"));
                
                Animal animal = new Animal(0, name, type, 0, skills);
                animal.setSkills(skills);
                
                animals.add(animal);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
