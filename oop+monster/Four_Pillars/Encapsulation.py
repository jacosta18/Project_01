# It is concidered standard or best practise to keep internal data or attributes as private
# as possible. Only a class should be a ble to have access to internal variables.

################################## FIRST LINE OF DEFENCE ##########################################################
#
# class Person():
#
#     def __init__(self,age,name,email,height):
#         self.__height = height
#         self.age = age
#         self.name = name
#         self.email  = email
#
#     def show(self):
#         #self.__height = 50
#         print(f"my name is {self.name} and i am {self.age} old and my email is{self.email} and {self.__height}")
#
#
# markson = Person(25,"Markson","joel@done.com",1.79)
# markson.show()
# markson.name = "Filipe"
# markson.show()
# markson.age = 30
# markson.show()
# markson.__height = 60   #  Python only hides from accidental outside changes not intensional
# #print(markson.__height) # This will crash
# #print(markson._Person__height) # This will not


########################################## SECOND LINE OF DEFENCE ###############################################



class Person():

    def __init__(self,age,name,email,height):
        self.__height = height
        self.age = age
        self.name = name
        self.email  = email

    def show(self):

        print(f"my name is {self.name} and i am {self.age} old and my email is{self.email} and {self.__height}")

    def set_height(self,value):
        if value > 9 or value < 0:
            self.__height = 4.5
        else:
            self.__height = value

    def get_height(self):
        return self.__height




markson = Person(25,"Markson","joel@done.com",45)
#markson.show()
#markson.name = "Filipe"
#markson.show()
#markson.age = 30
#markson.show()
#markson.__height = 60   #  Python only hides from accidental outside changes not intensional
#print(markson.__height) # This will crash
markson.show()
markson.set_height(200)
markson.show()
print(markson.get_height())



