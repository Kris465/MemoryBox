package Homework3.Goods2;

public class Goods2 {
    private String name;

    private String country;

    private Integer weight;

    private Double price;

    private Integer kind;

    public Goods2(String name, String country, Integer weight, Double price, Integer kind) {
        this.name = name;
        this.country = country;
        this.weight = weight;
        this.price = price;
        this.kind = kind;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public Integer getWeight() {
        return weight;
    }

    public void setWeight(Integer weight) {
        this.weight = weight;
    }

    public Double getPrice() {
        return price;
    }

    public void setPrice(Double price) {
        this.price = price;
    }

    public Integer getKind() {
        return kind;
    }

    public void setKind(Integer kind) {
        this.kind = kind;
    } 
}
