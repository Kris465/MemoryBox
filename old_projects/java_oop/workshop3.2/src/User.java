public class User implements Comparable<User> {
    
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

    @Override
    public int compareTo(User other) {
        int status1 = this.getStatus().compareTo(other.getStatus());
        if (status1 != 0) {
            return status1;
        }
        int name1 = this.getName().compareTo(other.getName());
        if (name1 != 0) {
            return name1;
        }

        return this.getSalary() - other.getSalary();
    }
}
