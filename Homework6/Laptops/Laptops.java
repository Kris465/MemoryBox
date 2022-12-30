package Homework6.Laptops;

public class Laptops {
    private Integer ram;

    private Integer hdd;

    private String os;

    private String colour;

    private Double size;

    public Laptops(Integer ram, Integer hdd, String os, String colour, Double size) {
        this.ram = ram;
        this.hdd = hdd;
        this.os = os;
        this.colour = colour;
        this.size = size;
    }

    public Integer getRam() {
        return ram;
    }

    public void setRam(Integer ram) {
        this.ram = ram;
    }

    public Integer getHdd() {
        return hdd;
    }

    public void setHdd(Integer hdd) {
        this.hdd = hdd;
    }

    public String getOs() {
        return os;
    }

    public void setOs(String os) {
        this.os = os;
    }

    public String getColour() {
        return colour;
    }

    public void setColour(String colour) {
        this.colour = colour;
    }

    public Double getSize() {
        return size;
    }

    public void setSize(Double size) {
        this.size = size;
    }

}
