import java.util.List;

public interface Actionable {
    
    List<Note> getAllNotes();
    String CreateNote(Note note);
    String EditNote(Note note);
    void DeleteNote(List<Note> notes);
}
