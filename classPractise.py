class Animal :
    ISALIVE = True # Butun objectlere aiddi if not changed for the specific object 

    def __init__(self, legs, tail, eyes) : # Constructor of class is always def __init__
        self.legs = legs
        self.tail = tail
        self.eyes = eyes
        self.__isAnimal = True  # When defining a private variable write __ before var name
   
    def info(self) :
        print(f"This animal has {self.legs} legs, {self.eyes} eyes, and it does{'' if self.tail else ' not'} have a tail") 

# print(__name__)


if __name__ == "__main__" : # If the file is directly run = __main__, if imported, __name__ is the file name from which we import and the code in the if statement will not run
    a1 = Animal(4, True, 2)
    a2 = Animal(8, False, 8)

    # a1.info()
    Animal.info(a1)
    a2.info()
    Animal.ISALIVE = False # Changes ISALIVE for all objects
    print(a1.ISALIVE)
    print(a2.ISALIVE)
    a1.hands = 5
    print(a1.hands)