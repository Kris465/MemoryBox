package solid;

import solid.srp.Point;
import solid.srp.Square;
import solid.srp.SquareView;

public class Main {
    public static void main(String[] args) {
        Square square = new Square(new Point(1,1), 5);
        System.out.printf("Площадь фигуры: %d \n", square.getArea());
        SquareView squareZoom = new SquareView(5);
        squareZoom.draw(1);
    }
}
