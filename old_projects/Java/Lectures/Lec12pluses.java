package Lectures;

public class Lec12pluses {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 1_000_000; i++) {
        sb.append("+");
        System.out.print(sb);
        }       
    }
}
