from math import log, sin, cos, radians


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum_up(self):
        return self.num1 + self.num2

    def minus(self):
        return self.num1 - self.num2

    def ymnoz(self):
        return self.num1 * self.num2

    def delen(self):
        return self.num1 / self.num2

    def v_stepen(self):
        return self.num1 ** self.num2

    def korenb(self):
        return self.num1 ** 0.5

    def module(self):
        return abs(self.num1)

    def log(self):
        return log(self.num2, self.num1)

    def sin(self):
        return sin(radians(self.num1))

    def cos(self):
        return cos(radians(self.num1))

    def okryglenie(self):
        return round(self.num1, 2)
