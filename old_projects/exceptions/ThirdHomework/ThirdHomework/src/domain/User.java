package domain;

import java.time.LocalDate;

public class User {
    private String name;
    private String surname;
    private String patronymic;
    private LocalDate dateOfBirth;
    private String phoneNumber;
    private char gender;;
    
    public User() {}

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    public String getPatronymic() {
        return patronymic;
    }

    public void setPatronymic(String patronymic) {
        this.patronymic = patronymic;
    }

    public LocalDate getDateOfBirth() {
        return dateOfBirth;
    }

    public void setDateOfBirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        if (phoneNumber.matches("\\d{10}")) {
            this.phoneNumber = phoneNumber;
        } else {
            throw new IllegalArgumentException("Invalid phone number format.");
        }
    }

    public char getGender() {
        return gender;
    }

    public void setGender(char gender) {
         if (gender == 'm' || gender == 'f') {
        this.gender = gender;
        } else {
            throw new IllegalArgumentException("Invalid gender.");
        }
    }

    @Override
    public String toString() {
        return surname + " " + name + " " + patronymic + " " + dateOfBirth + " " + phoneNumber + " " + gender;
    }
}
