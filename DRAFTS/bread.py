class Bread:
    
    price = 10
    weight = 100

    def __init__(self, name, price, weight):
        self.name = name
        self.personal_price = price
        self.personal_weight = weight

        if self.personal_price >= 1.5 * self.price:
            Bread.price_update(self.personal_price)


    @classmethod
    def price_update(cls, new_price):
        cls.price = new_price

    def show_info(self):
        print(f"Name: {self.name}, price: {self.personal_price}, weight: {self.personal_weight}, in general: {self.price}")

chiabbata = Bread("Chiabbata", 12, 100)
chiabbata.show_info()
labagett = Bread("LaBagett", 16, 100)
labagett.show_info()
bulka = Bread("Bulka", 8, 100)
bulka.show_info()
