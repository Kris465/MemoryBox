import java.util.Collections;

public class App {
    public static void main(String[] args) throws Exception {
        Staff staff = new Staff();

        staff.addUser(new User("John", "Smith", 26));
        staff.addUser(new User("Jerry", "Black", 34));
        staff.addUser(new User("Jenifer", "White", 19));
        staff.addUser(new User("Brus", "Black", 29));
        staff.addUser(new User("Jenifer", "White", 14));

        for (User user : staff) {
            System.out.println(user);
        }

        // А теперь сортируем...
        System.out.println("_____________");

        Collections.sort(staff.getUsers());

        for (User user : staff) {
            System.out.println(user);
        }
    }
}
