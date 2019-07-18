from Four_Pillars.Abstraction import Reptiles

class Snake(Reptiles):
    def __init__(self, age, weight,specie,name,region_found,number_of_fangs,length):
        super().__init__(age, weight,specie,name,region_found)
        self.number_of_fangs = number_of_fangs
        self.length = length

    def can_constrict(self,bool_value):
        return bool_value

    def can_swim(self,bool_value):
        return bool_value

python =Snake(35,450,"pythoras terroriza","Bop","Morgate",0,12)

print(python.length)
print(python.specie)
print(python.region_found)
print(python.number_of_fangs)
print(python.age)
python.age = -35
print(python.age)
print(python.can_constrict(True))



