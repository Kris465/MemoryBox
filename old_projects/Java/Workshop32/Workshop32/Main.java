package Workshop32;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Students Student1 = new Students("Иванов", 5, 1700.0, 2);
        Students Student2 = new Students("Петров", 6, 1550.6, 3);
        Students Student3 = new Students("Сидорова", 7, 2300.2, 5);
        Students Student4 = new Students("Лукьянова", 7, 1263.2, 3);
        List<Students> listStudents = new ArrayList<>();
        listStudents.add(Student1);
        listStudents.add(Student2);
        listStudents.add(Student3);
        listStudents.add(Student4);
        for (int i = 0; i < listStudents.size(); i++) {
            Students Students = listStudents.get(i);
            if ((Students.getMark() >= 2) && (Students.getMark() <= 5) && 
                    (Students.getMark() % 2 == 1) && (Students.getSurName().endsWith("ова"))) {
                System.out.println("Students: " + Students.getSurName() + " salary " + Students.getSalary());
            }
        }
    } 
}
