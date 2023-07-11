import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Counter {
    private int idCounter;
    private File file;

    public Counter(String fileName) {
        this.file = new File(fileName);
        this.idCounter = 1;
    }

    public int getNextId() {
        if (file.exists()) {
            try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
                String line;
                String lastLine = null;
                while ((line = reader.readLine()) != null) {
                    lastLine = line;
                }
                if (lastLine != null) {
                    String[] parts = lastLine.split(", ");
                    int highestId = Integer.parseInt(parts[0]);
                    idCounter = highestId + 1;
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        } else {
            idCounter++;
        }
        return idCounter;
    }
}
