public class User {

    private String name;
    private String status;
    private int salary;

    public User(String name, String status, int salary) {
        this.name = name;
        this.status = status;
        this.salary = salary;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }

    @Override
    public String toString() {
        return String.format("Name: %s, Status: %s, Salary: %d", name, status, salary);
    }
}
