package personal.controllers;

import personal.model.Repository;
import personal.model.User;

import java.util.List;

public class UserController {
    private final Repository repository;

    public UserController(Repository repository) {
        this.repository = repository;
    }

    public void saveUser(User user) {
        repository.CreateUser(user);
    }

    public User readUser(String userId) throws Exception {
        List<User> users = repository.getAllUsers();
        for (User user : users) {
            if (user.getId().equals(userId)) {
                return user;
            }
        }

        throw new Exception("User not found");
    }

    public void deleteUser(String userId) throws Exception {
        List<User> users = repository.getAllUsers();
        User removedUser = null;;
        for (User user : users) {
            if (user.getId().equals(userId)) {
                removedUser = user;
            }
        }
        users.remove(removedUser);
        repository.DeleteUser(users);
    }
}
