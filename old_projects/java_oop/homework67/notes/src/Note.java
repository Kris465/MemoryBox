public class Note {
    
    private String id = "";
    private String title;
    private String text;
    
    public Note(String title, String text) {
        this.title = title;
        this.text = text;
    }

    public Note(String id, String title, String text) {
        this.id = id;
        this.title = title;
        this.text = text;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    @Override
    public String toString() {
        return "Note № " + id + " title: " + title + " text: " + text;
    }
}
