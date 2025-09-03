import java.util.Collections;

public class App {
    public static void main(String[] args) throws Exception {
        Staff staff = new Staff();
        staff.addUser(new User("John", "boss", 100));
        staff.addUser(new User("Sean", "manager", 40));
        staff.addUser(new User("Merry", "manager", 50));
        staff.addUser(new User("Chris", "sysadmin", 40));
        staff.addUser(new User("John", "manager", 20));
        staff.addUser(new User("Sean", "manager", 40));
        staff.addUser(new User("Merry", "manager", 50));
        staff.addUser(new User("Shoun", "devoper", 30));

        for (User user : staff) {
            System.out.println(user);
        }
    
        System.out.println("____________");
        Collections.sort(staff.getUsers());

        for (User user : staff) {
            System.out.println(user);
        }
    }
}
