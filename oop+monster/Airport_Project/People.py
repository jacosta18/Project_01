
class People():

    def __init__(self, name, __passport):
        self.name = name
        self.__passport = __passport

    def can_complain(self):
        return "This is poor service!!"

    def be_sick(self):
        return "Bluuurrrghhh!"

    def be_scared(self,bool_value):
        return bool_value

class staff (People):   # Subclass of People

    def __init__(self,name, passport, emp_id, occupation):
        super().__init__(name, passport)
        self.emp_id = emp_id
        self.occupation = occupation



person_1 = People("Adam Perumal", "AC039459ZB")
person_1 = People("Adam Perumal", "AC039459ZB")

staff_1 = People("Omid Flynn", "B32094564D",100687,occupation)

print(staff_1)
print(person_1.be_scared(False))
print(person_1.be_sick())
print(person_1.can_complain())