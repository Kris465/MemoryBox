package diploma.task2;

import java.time.LocalDateTime;

public class Note {
    private final String title;
    private final String content;
    private LocalDateTime timestamp;

    public Note(String title, String content) {
        this.title = title;
        this.content = content;
        this.timestamp = LocalDateTime.now();
    }

    public String getTitle() {
        return title;
    }

    public String getContent() {
        return content;
    }

    public LocalDateTime getTimestamp() {
        return timestamp;
    }

    @Override
    public String toString() {
        return "Title: " + title + "\nContent: " + content + "\nTimestamp: " + timestamp + "\n";
    }
}