package diploma.task2;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class NoteManager {
    private final List<Note> notes;
    private final String filePath;

    public NoteManager(String filePath) {
        this.notes = new ArrayList<>();
        this.filePath = filePath;
        loadNotes();
    }

    public void addNote(Note note) {
        notes.add(note);
        saveNotes();
    }

    public List<Note> getNotes() {
        return notes;
    }

    public void saveNotes() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            for (Note note : notes) {
                writer.write(note.getTitle() + "|" + note.getContent() + "|" + note.getTimestamp());
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void loadNotes() {
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split("\\|");
                if (parts.length == 3) {
                    Note note = new Note(parts[0], parts[1]);
                    notes.add(note);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
