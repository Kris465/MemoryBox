package diploma.task3;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        TaskList taskList = new TaskList("tasks.txt");

        while (true) {
            System.out.println("1. Add a task");
            System.out.println("2. Delete the task");
            System.out.println("3. Mark the task as done");
            System.out.println("4. Show all tasks");
            System.out.println("5. Show all done tasks");
            System.out.println("6. Exit");
            System.out.print("Choose an action: ");
            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    System.out.print("Input the name of the task: ");
                    String title = scanner.nextLine();
                    taskList.addTask(new Task(title));
                    break;
                case 2:
                    System.out.print("Input the id of the task for deleting: ");
                    int removeIndex = scanner.nextInt() - 1;
                    taskList.removeTask(removeIndex);
                    break;
                case 3:
                    System.out.print("Input the id of the task to mark as done: ");
                    int completeIndex = scanner.nextInt() - 1;
                    taskList.markTaskAsCompleted(completeIndex);
                    break;
                case 4:
                    System.out.println("All tasks:");
                    for (int i = 0; i < taskList.getTasks().size(); i++) {
                        System.out.println((i + 1) + ". " + taskList.getTasks().get(i));
                    }
                    break;
                case 5:
                    System.out.println("All done tasks:");
                    for (int i = 0; i < taskList.getCompletedTasks().size(); i++) {
                        System.out.println((i + 1) + ". " + taskList.getCompletedTasks().get(i));
                    }
                    break;
                case 6:
                    System.out.println("Exit");
                    scanner.close();
                    return;
                default:
                    System.out.println("Incorrect choice. Try again.");
            }
        }
    }
}