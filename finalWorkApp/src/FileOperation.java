import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class FileOperation {
    public List<Animal> readFromFile(String filename) {
        List<Animal> animals = new ArrayList<>();
        
        try (Scanner scanner = new Scanner(new File(filename))) {
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] parts = line.split(",");
                
                int id = Integer.parseInt(parts[0]);
                String name = parts[1];
                String type = parts[2];
                int age = Integer.parseInt(parts[3]);
                List<String> skills = Arrays.asList(parts[4].split(";"));
                
                Animal animal = new Animal(id, name, type, age, skills);
                animals.add(animal);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        
        return animals;
    }
    
    public void writeToFile(List<Animal> animals, String filename) {
        if (animals == null) {
            return;
        }
        
        try (PrintWriter writer = new PrintWriter(new FileWriter(filename))) {
            for (Animal animal : animals) {
                writer.println(animal.getId() + "," + animal.getName() + "," + animal.getType() + "," + animal.getAge() + "," + String.join(";", animal.getSkills()));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
