import java.util.HashSet;
import java.util.Set;

public class task2 {
    // Определить, есть ли вы массиве дубликаты, если найден хоть один, вывести на экран(true), в противном случае (false).
    // public static void main(String[] args) {
    //     int [] arr = new int[]{1, 2, 3, 4, 5, 6, 7, 8, 4};
    //     Set<Integer> set = new HashSet<>();
    //     boolean f = false;
    //     for (int i = 0; i < arr.length; i++) {
    //         if (set.contains(arr[i])) {
    //             f = true;
    //             break;
    //         } else {
    //             set.add(arr[i]);
    //         }
    //     }
    //     System.out.println(f);       
    // }

    public static void main(String[] args) {
        int [] arr = new int[]{1, 2, 3, 4, 5, 6, 7, 8};
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < arr.length; i++) {
            if (set.contains(arr[i])) {
                set.add(arr[i]);
            }
        }
        if (arr.length != set.size()) {
            System.out.println("true");
        } else {
            System.out.println("false");
        }
    }
}





