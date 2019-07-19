# It is considered standard or best practise to keep internal data or attributes as private
# as possible. Only a class should be a ble to have access to internal variables.

# Encapsulation is particularly important when you want to give your code to other people!
# Because they could then try and change your code.

# Encapsulation is particularly important when you want to give your code to other people!
# Because they could then try and change your code.


#----------------------------------------------------First Stage---------------------------------------------
#
class Car:
    def __init__(self, speed, colour):
       self.speed = speed
       self.colour = colour

    def set_speed(self,value):
        self.speed = value

    def get_speed(self):
         return self.speed

ford = Car(210, "Black")
audi = Car(350, "White")
honda = Car (300, "Grey")


ford.speed = 400

print(ford.get_speed())
print(ford.colour)


#-------------------------------------------Second Stage---------------------------------------------------------------------

# class Hello:
#
#     def __init__(self,name):
#         self.a = 10
#         self._b = 20
#         self.__c = 30
#
# hello = Hello('name')
# print(hello.a)
# print(hello._b)
# print(hello.__c)


#------------------------------------------------------------- Third Stage ---------------------------------------------------------

# class Car:
#     def __init__(self, speed, colour):
#         self.__speed = speed
#         self.__colour = colour
#
#     def set_speed(self,value):
#         self.__speed = value
#
#     def get_speed(self):
#         return self.__speed
#
# ford = Car(210, "Black")
# audi = Car(350, "White")
# honda = Car (300, "Grey")
#
#
#
# ford.speed = 500
#
# print(ford.get_speed())
# print(ford.colour)




















