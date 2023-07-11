package domain;

import java.util.ArrayList;
import java.util.List;

public class CurrentAnimal extends Animal implements Skills{

    private List<String> skills;

    public CurrentAnimal(int id, String name, int age, String type, List<String> skills) {
        super(id, name, age, type);
        this.skills = new ArrayList<>();
    }

    @Override
    public List<String> getSkills() {
        return skills;
    }

    @Override
    public void addSkill(String skill) {
        skills.add(skill);
    }

    @Override
    public void removeSkill(String skill) {
        skills.remove(skill);
    }
}
