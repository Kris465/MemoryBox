import java.util.Iterator;

public class App {
    public static void main(String[] args) throws Exception {
        Table table1 = new Table(null);

        Ingredient ingredients1 = new Ingredient("water", 10);
        Ingredient ingredients2 = new Ingredient("butter", 6);
        Ingredient ingredients3 = new Ingredient("coffee", 7);
        Dish porridge = new Dish("Porridge", ingredients1, 60);
        Dish sandwich = new Dish("Sandwich", ingredients2, 16);
        Drink coffee = new Drink("Coffee", ingredients3, 22);

        table1.addUserChoice(porridge);
        table1.addUserChoice(sandwich);
        table1.addUserChoice(coffee);
        table1.addUserChoice(ingredients1);
        table1.addUserChoice(ingredients2);
        table1.addUserChoice(ingredients3);

        Iterator dishes = table1;
        while(dishes.hasNext()) {
            System.out.println(table1.next());
        }
    }
}
