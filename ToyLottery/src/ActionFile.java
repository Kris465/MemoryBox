import java.util.ArrayList;
import java.util.List;

public class ActionFile implements Action {

    private Mapper mapper = new Mapper();
    private FileOperation fileOperation;

    public ActionFile(FileOperation fileOperation) {
        this.fileOperation = fileOperation;
    }

    @Override
    public void addPrize(Toy toy) {
        List<Toy> toys = getAllPrizes();
        toys.add(toy);
        List<String> lines = new ArrayList<>();
        for (Toy item : toys) {
            lines.add(mapper.map(item));
        }
        fileOperation.saveAllLines(lines);
    }

    @Override
    public List<Toy> getAllPrizes() {
        List<String> lines = fileOperation.readAllLines();
        List<Toy> toys = new ArrayList<>();
        for (String line : lines) {
            toys.add(mapper.map(line));
        }
        return toys;
    }

    @Override
    public void saveAllLines(List<Toy> toys) {
        List<String> lines = new ArrayList<>();
        for (Toy item : toys) {
            lines.add(mapper.map(item));
        }
        fileOperation.saveAllLines(lines);
    }
}
