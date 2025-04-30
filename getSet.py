class Person:
    def __init__(self, frst_name, last_name):
        self.__frst_name = frst_name
        self.__last_name = last_name
    
    # Classic way Getter
    def getName(self):
        return self.__frst_name
    # Classic way Setter
    def setName(self, new_frst_name):
        self.__frst_name = new_frst_name

    # Pythonic way of Getter and Setter
    @property
    def familya(self):
        return self.__last_name

    @familya.setter
    def familya(self, new_last_name):
        self.__last_name = new_last_name

    # Info method
    def info(self):
        print(f"Info about person: {self.__frst_name} {self.__last_name}")


p = Person("Lala", "Alimova")
p.info()
p.familya = "Isgandarova" 
p.info()