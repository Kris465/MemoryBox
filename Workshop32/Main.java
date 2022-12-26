package Workshop32;

import java.util.*;

import Workshop32.Class.*;

public class Main {
    public static void main(String[] args) {
        Student student1 = new Student("Иванов", 5, 1700.0, 2);
        Student student2 = new Student("Петров", 6, 1550.6, 3);
        Student student3 = new Student("Сидорова", 7, 2300.2, 5);
        Student student4 = new Student("Лукьянова", 7, 1263.2, 3);
        List<Student> listStudent = new ArrayList<>();
        listStudent.add(student1);
        listStudent.add(student2);
        listStudent.add(student3);
        listStudent.add(student4);
        for (int i = 0; i < listStudent.size(); i++) {
            Student student = listStudent.get(i);
            if ((student.getMark() >= 2) && (student.getMark() <= 5) && 
                    (student.getMark() % 2 == 1) && (student.getSurName().endsWith("ова"))) {
                System.out.println("Student: " + student.getSurName() + " salary " + student.getSalary());
            }
        }
    } 
}
