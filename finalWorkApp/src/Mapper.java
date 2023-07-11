import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Mapper {
    public void saveToFile(List<CurrentAnimal> animals, String filename) {
        try (PrintWriter writer = new PrintWriter(new FileWriter(filename))) {
            for (CurrentAnimal animal : animals) {
                writer.println(map(animal));
            }
        } catch (IOException e) {
            System.out.println("Error saving to file: " + e.getMessage());
        }
    }

    public List<CurrentAnimal> readFromFile(String filename) {
        List<CurrentAnimal> animals = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = reader.readLine()) != null) {
                animals.add(map(line));
            }
        } catch (IOException e) {
            System.out.println("Error reading from file: " + e.getMessage());
        }
        return animals;
    }

    public String map(CurrentAnimal currentAnimal) {
        StringBuilder sb = new StringBuilder();
        sb.append(currentAnimal.getId()).append(", ");
        sb.append(currentAnimal.getName()).append(", ");
        sb.append(currentAnimal.getAge()).append(", ");
        sb.append(currentAnimal.getType()).append(", ");
        List<String> skills = currentAnimal.getSkills();
        for (String skill : skills) {
            sb.append(skill).append(", ");
        }
        return sb.toString();
    }

    public CurrentAnimal map(String line) {
        String[] lines = line.split(", ");
        int id = Integer.valueOf(lines[0]);
        String name = lines[1];
        int age = Integer.valueOf(lines[2]);
        String type = lines[3];
        CurrentAnimal currentAnimal = new CurrentAnimal(id, name, age, type);
        for (int i = 4; i < lines.length; i++) {
            currentAnimal.addSkill(lines[i]);
        }
        return currentAnimal;
    }
}
