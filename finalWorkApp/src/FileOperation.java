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
        File file = new File(filename);
    
        if (file.exists()) {
            try (Scanner scanner = new Scanner(new File(filename))) {
                while (scanner.hasNextLine()) {
                    String line = scanner.nextLine();
                    String[] parts = line.split(",");
    
                    int id;
                    try {
                        id = Integer.parseInt(parts[0]);
                    } catch (NumberFormatException e) {
                        id = 0;
                        continue;
                    }
                    String name = parts[1];
                    String type = parts[2];
                    int age;
                    try {
                        age = Integer.parseInt(parts[3]);
                    } catch (NumberFormatException e) {
                        age = 0;
                        continue;
                    }
                    List<String> skills;
                    if (parts.length > 4 && !parts[4].isEmpty()) {
                        skills = Arrays.asList(parts[4].split(";"));
                    } else {
                        skills = new ArrayList<>();
                    }
    
                    Animal animal = new Animal(id, name, type, age, skills);
                    animals.add(animal);
                }
            } catch (FileNotFoundException e) {
                e.printStackTrace();
    
            }
        }
        return animals;
    }

    public void writeToFile(List<Animal> animals, String filename) {
        try (PrintWriter writer = new PrintWriter(new FileWriter(filename))) {
            for (Animal animal : animals) {
                System.out.println(animal.toString());
                StringBuilder skillsBuilder = new StringBuilder();
                List<String> skills = animal.getSkills();
                if (skills != null && !skills.isEmpty()) {
                    for (String skill : skills) {
                        skillsBuilder.append(skill).append(";");
                    }
                    String skillsString = skillsBuilder.toString();
                    if (skillsString.endsWith(";")) {
                        skillsString = skillsString.substring(0, skillsString.length() - 1);
                    }
                    writer.println(animal.getId() + "," + animal.getName() + "," + animal.getType() + "," + animal.getAge()
                            + "," + skillsString);
                } else {
                    writer.println(animal.getId() + "," + animal.getName() + "," + animal.getType() + "," + animal.getAge()
                            + ",");
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}