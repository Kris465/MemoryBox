class Shape:

    def Square(self):
        print("Данный метод не определен для текущего класса")

class Circle(Shape):

    name = "Circle"

    def __init__(self, radius):
        self.radius = radius

    def Square(self):
        print(f"Площадь данной окружности равна: ", 3.14 * self.radius ** 2)

# a = Circle(10)
# b = Circle(15)
# a.Square()
b = Circle(10).Square()
