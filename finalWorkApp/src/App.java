import java.util.List;

import interfaceAdapters.ConsoleAdapter;
import interfaceAdapters.DatabaseAdapter.Mapper;
import useCases.AddAnimal;
import useCases.EditAnimalType;
import useCases.TeachAnimal;

public class App {
    public static void main(String[] agrs) {
        AddAnimal addAnimal = new AddAnimal();
        EditAnimalType editAnimalType = new EditAnimalType();
        TeachAnimal teachAnimal = new TeachAnimal();
        ConsoleAdapter consoleAdapter = new ConsoleAdapter(addAnimal, editAnimalType, teachAnimal);
    }
}
