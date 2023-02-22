import java.util.Iterator;

public class App {
    public static void main(String[] args) throws Exception {
        
        DoublyLinkedList list = new DoublyLinkedList();
        list.add("data1");
        list.add("data2");

        list.add(1, "data2_1");


        Iterator<String> iterator = list.iterator();
        while (iterator.hasNext()){
            String element = iterator.next();
            System.out.println(element);
        }
    }
}
