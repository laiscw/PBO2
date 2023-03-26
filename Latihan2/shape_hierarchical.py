class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def get_name(self):
        return self.name
    def get_color(self):
        return self.color
    def data(self):
        print(f"{self.name} data")
    
class TwoDimensional(Shape):
    def __init__(self, name, color, sides):
        super().__init__(name, color)
        self.sides = sides
    def get_sides(self):
        return self.sides
    
class ThreeDimensional(Shape):
    def __init__(self, name, color, merk):
        super().__init__(name, color)
        self.merk = merk
    def get_merk(self):
        return self.merk
    
# Hierarchical Inheritance
class Sphere(ThreeDimensional):
    def __init__(self, name, color, merk, price):
        super().__init__(name, color, merk)
        self.price = price
    def get_price(self):
        return self.price
    def data(self):
        print(f"{self.name} berwarna {self.color} dg merek {self.merk} berharga {self.price}")
        print("="*54)

Shape = Sphere("Volly Ball", "Yellow-Green", "Copaya BV100 Fun", "Rp 200.000")
Shape.data()
