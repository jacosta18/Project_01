#### The weakest points ###

# Given the user only the information needed to perform a task
# While keeping unnecesary information away
# Using python modules as an exampleof abstraction



# Four pillars of Object Oriented Programming
# Inheriatance

##### MOST FUNDAMENTAL POINT #####

class Animaml():  ## super class of truck

    def __init__(self,age, weight, specie):
        self.age = age      # same as age = 15 in oop
        self.weight= weight
        self.specie = specie

    def can_hunt(self,value):
       return value

    def eat(self):
       return "yum yum yum"

    def sleep(self):
       return "zzzzzzzzz"

class Mammal(Animaml):
    def __init__(self,age, weight, specie,name,can_speak):
        super().__init__(age,weight, specie)
        self.name = name
        self.can_speak = can_speak

    def can_speak_language(self,can_speak):
        return can_speak

class Bird (Animaml):
    def __init__(self,age, weight, specie,name,feather_color):
        super().__init__(age,weight, specie)
        self.name = name
        self.feather_color = feather_color

    def can_fly(self,can_fly):
        return can_fly

class Reptiles (Animaml):
    def __init__(self, age, weight, specie, name, region_found):
        super(). __init__(age,weight,specie)
        self.name = name
        self.region_found = region_found

    def is_venomous(self,value):
        return value


