class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def get_name(self):
        return self.name
    def get_color(self):
        return self.color
    def data(self):
        print(f"{self.name} data")

class Mammal(Animal):
    def __init__(self, name, color, fur):
        super().__init__(name, color)
        self.fur = fur
    def get_fur(self):
        return self.fur
    
class Bird(Animal):
    def __init__(self, name, color, wingspan):
        super().__init__(name, color)
        self.wingspan = wingspan
    def get_wingspan(self):
        return self.wingspan
    
# Hierarchical Inheritance
class Reptile(Mammal):
    def __init__(self, name, color, fur, Weight):
        super().__init__(name, color, fur)
        self.Weight = Weight
    def get_Weight(self):
        return self.Weight
    def data(self):
        print(f"{self.name} Berwarna {self.color} tipe bulu {self.fur} dengan berat {self.Weight}")
        print("="*54)
    
Mammal = Reptile("Mochi", "White", "Bicolor", "6.5 kg")
Mammal.data()