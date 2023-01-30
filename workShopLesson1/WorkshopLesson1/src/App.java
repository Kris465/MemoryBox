public class App {
    public static void main(String[] args) throws Exception {
        VendingMachine vendingMachine = new VendingMachine();
        vendingMachine.getProductList().add(new Product(20, "Apple"));
        vendingMachine.getProductList().add(new Product(30, "Pineapple"));
        vendingMachine.getProductList().add(new Product(40, "Apple pie"));
        vendingMachine.getProductList().add(new Product(50, "Apple juice"));
        vendingMachine.getProductList().add(new ChocolateBar(34, "Mars", 23));
        vendingMachine.getProductList().add(new GreatChocolateBar(34, "BigMars", 23, TypeSize.BIG));
        vendingMachine.getProductList().add(new Coffee(50, "Cappuccino", true));

        for(Product product : vendingMachine.getProductList()) {
            System.out.println(product);
        }

    }
}
