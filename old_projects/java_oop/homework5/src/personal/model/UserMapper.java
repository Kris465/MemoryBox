package personal.model;

public class UserMapper {
    public String map(User user) {
        return String.format("%s,%s,%s,%s", user.getId(), user.getFirstName(), user.getLastName(), user.getPhone());
    }

    public String map(User user, char delimiter) {
        return String.format("%s%s%s%s%s%s%s", user.getId(), delimiter, user.getFirstName(), delimiter, user.getLastName(), delimiter, user.getPhone());
    }

    public User map(String line) {
        char[] charArray = line.toCharArray();
        String findChar = ",";
        for (int i = 0; i < line.length(); i++) {
            if (!Character.isDigit(charArray[i])){
                char ch = charArray[i];
                findChar = Character.toString(ch);
            }
        }
        
        String[] lines = line.split(findChar);
        return new User(lines[0], lines[1], lines[2], lines[3]);
    }
}
