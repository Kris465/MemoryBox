public class Mapper {
    
    public String map(Toy toy) {
        return String.format("%s, %s, %s, %s", toy.getId(), toy.getName(), toy.getSize(), toy.getColour());
    }

    public Toy map(String line) {
        String[] lines = line.split(", ");
        return new Toy(Integer.valueOf(lines[0]), lines[1], Integer.valueOf(lines[2]), lines[3]);
    }
}
