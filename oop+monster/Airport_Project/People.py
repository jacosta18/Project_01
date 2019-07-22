
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

    def show(self):
        self.__passport = "AC039459ZB"
        print(f"My name is {self.name} and my passport number is {self.__passport}")


passenger_01= People("Adam Perumal","AC039459ZB")
# passenger_01.show()
# passenger_01.name = People("Alan Perumal")
# passenger_01.show()


class Staff (People):   # Subclass of People

    def __init__(self,name, passport, emp_id, occupation):
        super().__init__(name, passport)
        self.emp_id = emp_id
        self.occupation = occupation

    def safety_guide(self):
        return "In case of an emergency please ..."

person_1 = People("Adam Perumal", "AC039459ZB")
person_1 = People("Adam Perumal", "AC039459ZB")

staff_1 = Staff("Omid Flynn", "B32094564D",100687,"flight attendant")

# print(staff_1.be_scared(False))
# print(person_1.be_scared(True))
# print(person_1.be_sick())
# print(person_1.can_complain())
# print(staff_1.safety_guide())