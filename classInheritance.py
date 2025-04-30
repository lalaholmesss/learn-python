# import classPractise
from classPractise import Animal # Same as import, accesses everything, but we can get the specific variable name

class Cat(Animal) : # inheritance
    def __init__(self, color) :
        # self.legs = 4
        # self.eyes = 2
        # self.tail = True
        self.color = color
        super().__init__(4, True, 2) # super() refers to the parent class Animal, we pass arguments in __init__()

    def info(self) : # polymorphism
        print(f"This is the {self.color}-colored cat")
        super().info() # calls info() method of the parent class

c = Cat("white")
c.info()
print(c.ISALIVE)