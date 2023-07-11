package useCases;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

import domain.CurrentAnimal;

public class AddAnimal {

    public void createAnimal(int id, String name, int age, String type, List<String> skills) {

        CurrentAnimal currentAnimal = new CurrentAnimal(id, name, age, type, skills);

        try (BufferedWriter writer = new BufferedWriter(new FileWriter("animals.txt", true))) {
            writer.write(currentAnimal.toString());
            writer.newLine();
            System.out.println("Животное успешно создано и записано в файл.");
        } catch (IOException e) {
            System.out.println("Ошибка при записи в файл.");
        }
    }
}
