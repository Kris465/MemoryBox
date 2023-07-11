package domain;

import java.util.List;

public interface Skills {
    List<String> getSkills();
    void addSkill(String skill);
    void removeSkill(String skill);
}
