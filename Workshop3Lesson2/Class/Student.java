package Workshop3Lesson2.Class;

public class Student {
    private String surName;

    private Integer groupNumber;

    private Double salary;

    private Integer mark;

    public Student(String surName, Integer groupNumber, Double salary, Integer mark) {
        this.surName = surName;
        this.groupNumber = groupNumber;
        this.salary = salary;
        this.mark = mark;
    }

    public String getSurName() {
        return surName;
    }

    public void setSurName(String surName) {
        this.surName = surName;
    }

    public Integer getGroupNumber() {
        return groupNumber;
    }

    public void setGroupNumber(Integer groupNumber) {
        this.groupNumber = groupNumber;
    }

    public Double getSalary() {
        return salary;
    }

    public void setSalary(Double salary) {
        this.salary = salary;
    }

    public Integer getMark() {
        return mark;
    }

    public void setMark(Integer mark) {
        this.mark = mark;
    }
}
