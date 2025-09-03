public class App {
    
    public static void main()  {
        VendingMachine vendingMachine = new VendingMachine();
        vendingMachine.getPorductList().add(new Product(10, "Apple"));
        vendingMachine.getPorductList().add(new Product(20, "Pineapple"));
        vendingMachine.getPorductList().add(new Product(30, "Applepie"));
        
        for(Product product : vendingMachine.getPorductList()) {
            System.out.println(product.getName() + ": " + product.getCost());
        }
    }
}
