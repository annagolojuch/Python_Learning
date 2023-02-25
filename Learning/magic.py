import math


class Punkt2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.odleglosc = math.sqrt(x**2 + y**2)

    def __add__(self, other):
        return Punkt2D(self.x + other.x, self.y + other.y)


p1 = Punkt2D(2, 5)
p2 = Punkt2D(3, 4)
p3 = p1 + p2

print(p3.x, p3.y)
print(p1.odleglosc)
