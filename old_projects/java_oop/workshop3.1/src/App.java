public class App {
    public static void main(String[] args) throws Exception {
        
        Staff staff = new Staff();

        staff.addUser(new User("Merry", "manager", 15));
        staff.addUser(new User("James", "boss", 300));
        staff.addUser(new User("Karl", "sisadmin", 10));
        staff.addUser(new User("Rose", "artist", 40));

        for (User user : staff){
            System.out.println(user);
        }
    }
}
