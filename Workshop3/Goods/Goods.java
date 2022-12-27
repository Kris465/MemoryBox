package Workshop3.Goods;

// 1.	Даны сведения об экспортируемых товарах: 
// указывается наименование товара, страна, экспортирующая товар, 
// и объем поставляемой партии в штуках. Найти страны, 
// которые экспортируют данный товар, и общий объем его экспорта.

public class Goods {
    private String name;

    private String country;

    private Integer volume;


    public Goods(String name, String country, Integer volume) {
        this.name = name;
        this.country = country;
        this.volume = volume;
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

    public Integer getVolume() {
        return volume;
    }

    public void setVolume(Integer volume) {
        this.volume = volume;
    }
}

