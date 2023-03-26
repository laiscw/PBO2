class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} The animal speaks")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def bark(self):
        print(f"{self.breed} The dog barks")
        
class Bulldog(Dog):
    def __init__(self, name, breed, origin):
        super().__init__(name, breed)
        self.origin = origin
    def grow(self):
        print(f"{self.origin} The bulldog growls")
Bulldog = Bulldog("Yeontan", "Teacup Pomeranian", "Jerman")
Bulldog.speak() 
Bulldog.bark() 
Bulldog.grow() 

