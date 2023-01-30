public class App {

    public static void main(String[] args) throws Exception {
        VendingMachine vendingMachine = new VendingMachine();
        vendingMachine.getProductList().add(new Product(10, "Apple"));
        vendingMachine.getProductList().add(new Product(20, "Pineapple"));
        vendingMachine.getProductList().add(new Product(30, "Applepie"));
        vendingMachine.getProductList().add(new ChocolateBar(40, "Mars", 23.4));
        vendingMachine.getProductList().add(new GreatChocolateBar(50, "BigMars", 33, TypeSize.BIG));
        vendingMachine.getProductList().add(new Coffee(22, "Cappuccino", true));
        
        for(Product product : vendingMachine.getProductList()) {
            System.out.println(product);
        }
    }
}
