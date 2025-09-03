import java.util.List;

public class Controller {

    private final Repository repository;

    public Controller(Repository repository) {
        this.repository = repository;
    }

    public void saveNote(Note note) {
        repository.CreateNote(note);
    }

    public Note readNote(String id) throws Exception {
        List<Note> notes = repository.getAllNotes();
        for (Note note : notes) {
            if (note.getId().equals(id)) {
                return note;
            }
        }
        
        throw new Exception("Note was not found");

    }

    public void deleteNote(String id) {
        List<Note> notes = repository.getAllNotes();
        Note removedNote = null;
        for (Note note : notes) {
            if (note.getId().equals(id)) {
                removedNote = note;
            }
        }
        notes.remove(removedNote);
        repository.DeleteNote(notes);
    }

    public List<Note> show() {
        return repository.getAllNotes();
    }

    public void editNoteText(String id, String message) {
        List<Note> notes = repository.getAllNotes();
        for (Note note : notes) {
            if (note.getId().equals(id)) {
                note.setText(message);
            }
        }
        repository.SaveNotes(notes);
    }
}
