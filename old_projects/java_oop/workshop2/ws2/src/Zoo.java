import java.util.ArrayList;
import java.util.List;

public class Zoo {
    
    private ArrayList<Animal> animals;
    private Radio radio = new Radio();

    public Zoo() {
        animals = new ArrayList<>();
    }

    public Zoo addAnimal(Animal a) {
        animals.add(a);
        return this;
    }

    public List<Speakable> getSpeakables() {
        List<Speakable> answer = new ArrayList<Speakable>();
        
        for (Animal an : animals) {
            answer.add(an);
        }
        answer.add(radio);
        return answer;
    }

    public ArrayList<Animal> getAnimals() {
        return animals;
    }

    public List<Runable> getRunners() {
        List<Runable> result = new ArrayList<Runable>();

        for (Animal an: animals) {
            if(an instanceof Runable) {
                result.add((Runable) an);
            }
        }
        return result;
    }

    public int getChampionOfRunners() {
        int max = 0;
        for (Runable runner: getRunners()){
            if (max < runner.speedOfRun()) {
                max = runner.speedOfRun();
            }
        }
        return max;
    }

    public List<Flyable> getFlyers() {
        List<Flyable> result = new ArrayList<Flyable>();

        for (Animal an: animals) {
            if(an instanceof Flyable) {
                result.add((Flyable) an);
            }
        }
        return result;
    }

    public List<Swimable> getSwimmers() {
        List<Swimable> result = new ArrayList<Swimable>();

        for (Animal an: animals) {
            if(an instanceof Swimable) {
                result.add((Swimable) an);
            }
        }
        return result;
    }
}
