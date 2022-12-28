
import java.util.HashSet;
import java.util.Set;

public class task4 {
    public static void main(String[] args) {
        int[] nums1 = new int[]{1, 2, 3, 4};
        int[] nums2 = new int[]{3, 5, 3, 47, 2, 1, 5};
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < nums1.length; i++) {
            set.add(nums1[i]);
        }
        for (int i = 0; i < nums2.length; i++) {
            if (set.contains(nums2[i])) {
                System.out.println("Meaning is " + nums2[i]);
                set.remove(nums2[i]);
            }
        }
    }
}
