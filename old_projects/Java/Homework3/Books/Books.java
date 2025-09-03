package Homework3.Books;

public class Books {
    private String title;

    private String author;

    private Double price;

    private Integer year;

    private Integer pages;

    public Books(String title, String author, Double price, Integer year, Integer pages) {
        this.title = title;
        this.author = author;
        this.price = price;
        this.year = year;
        this.pages = pages;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public Double getPrice() {
        return price;
    }

    public void setPrice(Double price) {
        this.price = price;
    }

    public Integer getYear() {
        return year;
    }

    public void setYear(Integer year) {
        this.year = year;
    }

    public Integer getPages() {
        return pages;
    }

    public void setPages(Integer pages) {
        this.pages = pages;
    }

}
