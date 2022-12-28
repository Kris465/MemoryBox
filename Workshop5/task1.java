import java.util.HashMap;
import java.util.Map;

public class task1 {
// посчитать количество вхождений каждой буквы в текст
    public static void main(String[] args) {
        Map<Character, Integer> map = new HashMap<>();
        // Set<Integer> set = new HashSet<>();
        String str = "alksdfjd alsdkjfaldskfj lkajdfiojadf";
        for (int i = 0; i < str.length(); i++) {
            if (map.containsKey(str.charAt(i))) {
                map.put(str.charAt(i), map.get(str.charAt(i)) + 1);
            } else {
                map.put(str.charAt(i), 1);
            }
        }
        // for (var entry :map.entrySet())
        for (Map.Entry<Character, Integer> entry :map.entrySet()) {
            System.out.println("Буква - " + entry.getKey() + " ,встретилась " + entry.getValue());
        }
    }
}
