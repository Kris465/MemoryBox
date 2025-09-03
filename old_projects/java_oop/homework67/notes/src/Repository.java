import java.util.List;

public interface Repository {

    List<Note> getAllNotes();
    String CreateNote(Note note);
    void DeleteNote(List<Note> notes);
    void SaveNotes(List<Note> notes);
}
