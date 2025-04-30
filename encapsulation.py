class Person :
    def __init__(self, name, age) :
        self.__name  = name
        self.age = age
    
    def getName(self) : # To access the private variable outside of the class
        return self.__name

    def goToAsanXidmetAndChangeName(self, newName) : # To be able to change the variable outside of class by passing new argument
        self.__name = newName

p = Person("Lala", 19)
print(p.getName())
p.goToAsanXidmetAndChangeName("Hasan")
print(p.getName())
