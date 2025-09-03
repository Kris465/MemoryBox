import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Staff implements Iterable<User> { // Итератор???

    private List<User> users = new ArrayList<>();

    public void addUser(User user) {
        users.add(user);
    }

    public List<User> getUsers() {
        return users;
    }

    @Override
    public Iterator<User> iterator() {

        return new Iterator<User>() {

            private int currentIndex = 0;// Поле, которое содержит индекс текущего элемента

            @Override
            public boolean hasNext() { // Определяет, есть ли у него следующий элемент
                return users.size() > currentIndex; // сравниваем текущий элемент с размером
            }

            @Override
            public User next() { // Получить следующий элемент
                return users.get(currentIndex++);
            }

        }; // Точка с запятой относится к return, мы создали анонимный класс здесь
    }
    // Мы переписываем интерфейс, чтобы воспользоваться стандартными библиотеками.
    // Iterator - встроенная библиотека java и мы можем так переписывать все
    // библиотеки


}
