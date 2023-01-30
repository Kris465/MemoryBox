public class App {

    public static void main(String[] args) throws Exception {
        VendingMachine vendingMachine = new VendingMachine();
        vendingMachine.getProductList().add(new Product(10, "Apple"));
        vendingMachine.getProductList().add(new Product(20, "Pineapple"));
        vendingMachine.getProductList().add(new Product(30, "Applepie"));
        
        for(Product product : vendingMachine.getProductList()) {
            System.out.println(product.getName() + ": " + product.getCost());
        }
    }
}
