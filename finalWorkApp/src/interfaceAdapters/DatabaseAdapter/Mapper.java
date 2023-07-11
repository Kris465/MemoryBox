package interfaceAdapters.DatabaseAdapter;

import java.util.List;

import domain.CurrentAnimal;

public class Mapper {
    
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
