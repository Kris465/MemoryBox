package Workshop32;

public class Students {
    private String surName;

    private Integer groupNumber;

    private Double salary;

    private Integer Mark;

    public Students(String surName, Integer groupNumber, Double salary, Integer mark) {
        this.surName = surName;
        this.groupNumber = groupNumber;
        this.salary = salary;
        Mark = mark;
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
        return Mark;
    }

    public void setMark(Integer mark) {
        Mark = mark;
    }
}
