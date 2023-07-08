public class Mapper {
    
    public String map(CurrentAnimal currentAnimal) {
        return String.format("%s, %s, %s, %s", currentAnimal.getId(), currentAnimal.getName(), currentAnimal.getAge(), currentAnimal.getAction());
    }

    public CurrentAnimal map(String line) {
        String[] lines = line.split(", ");
        return new CurrentAnimal(Integer.valueOf(lines[0]), lines[1], Integer.valueOf(lines[2]), lines[3]);
    }
}
