import java.util.ArrayList;
import java.util.List;

public class Action implements Actionable {
    
    private Mapper mapper = new Mapper();
    private FileOperation fileOperation;

    public Action(Mapper mapper, FileOperation fileOperation) {
        this.mapper = mapper;
        this.fileOperation = fileOperation;
    }

    @Override
    public List<Note> getAllNotes() {
        List<String> lines = fileOperation.readAllLines();
        List<Note> Notes = new ArrayList<>();
        for (String line : lines) {
            Notes.add(mapper.map(line));
        }
        return Notes;
    }

    @Override
    public String CreateNote(Note Note) {

        List<Note> Notes = getAllNotes();
        int max = 0;
        for (Note item : Notes) {
            int id = Integer.parseInt(item.getId());
            if (max < id){
                max = id;
            }
        }
        int newId = max + 1;
        String id = String.format("%d", newId);
        Note.setId(id);
        Notes.add(Note);
        List<String> lines = new ArrayList<>();
        for (Note item: Notes) {
            lines.add(mapper.map(item));
        }
        fileOperation.saveAllLines(lines);
        return id;
    }

    @Override
    public void DeleteNote(List<Note> Notes) {
        List<String> lines = new ArrayList<>();
        for (Note item: Notes) {
            lines.add(mapper.map(item));
        }
        fileOperation.saveAllLines(lines);
    }
}
