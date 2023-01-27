package Sample2;

public class OtherFactory {
    
    private String product;
    private int number;
    private String quality;
    // private static int counter = 0; //статическое поле, благодаря которому будем выдавать уникальные значения объектам. Не зависят от состояния объекта, оно определено в самом классе.
    
    public OtherFactory(String product, int number, String quality) {
        this.product = product;
        this.number = number;
        this.quality = quality;

        //id = ++counter; // Сначала увеличиваем каунтер, а потом присваиваем это значение в переменную id
    }
    public String getProduct() {
        return product;
    }
    public void setProduct(String product) {
        this.product = product;
    }
    public int getNumber() {
        return number;
    }
    public void setNumber(int number) {
        this.number = number;
    }
    public String getQuality() {
        return quality;
    }
    public void setQuality(String quality) {
        this.quality = quality;
    }

    // void displayInfo() {
    //     System.out.printf("Id: %d\tProduct: %s\tNumber: %d\tQuality: %s\n",id, product, number, quality);
    // }
}
