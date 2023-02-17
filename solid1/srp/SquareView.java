package solid.srp;

public class SquareView {
    
    private int side;

    public SquareView(int side) {
        this.side = side;
    }

    public void draw(int zoom) {
        int newSide = side * zoom; 
        for (int i = 0; i < newSide; i++) {
            System.out.print("*");
        }
        System.out.println();
        for (int i = 0; i < newSide - 2; i++) {
            System.out.print("*");
            for (int j = 1; j < newSide - 1; j++) {
                System.out.print(" ");
            }
            System.out.println("*");
        }
        for (int i = 0; i < newSide; i++) {
            System.out.print("*");
        }
    }
}
