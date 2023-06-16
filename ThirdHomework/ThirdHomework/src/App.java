import java.lang.module.FindException;

import interfaceAdapters.ConsoleAdapter;
import useCases.CreateUser;
import useCases.FindUser;

public class App {
    
    public static void main(String[] agrs) {
        CreateUser createUser = new CreateUser();
        FindUser findUser = new FindUser();
        ConsoleAdapter consoleAdapter = new ConsoleAdapter(createUser, findUser);
        consoleAdapter.start();
    }
}
