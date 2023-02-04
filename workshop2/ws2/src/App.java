public class App {
    public static void main(String[] args) throws Exception {
        
        Zoo zoo1 = new Zoo();
        zoo1.addAnimal(new Cat("Vasya", 1, "grey"))
        .addAnimal(new Horse("Flower", 2))
        .addAnimal(new Duck("Donald", 3))
        .addAnimal(new Mermaid("Rose", 4));
        
        for (Animal an: zoo1.getAnimals()) {
            System.out.println(an);
            System.out.println(an.say());
        }

        System.out.println("Sounds of the zoo");

        for (Speakable speak : zoo1.getSpeakables()){
            System.out.println(speak.say());
        }

        for (Runable runner : zoo1.getRunners()){
            System.out.println("Speed is " + runner.speedOfRun());
        }

        int max = zoo1.getChampionOfRunners();
        System.out.println(String.format("Max of speed in the zoo is %d", max));

        for (Flyable flyer: zoo1.getFlyers()) {
            System.out.println("Speed of flying: " + flyer.speedOfFly());
        }

        for (Swimable swimmer: zoo1.getSwimmers()) {
            System.out.println("Speed of swimming is " + swimmer.speedOfSwim());
        }
    }
}
