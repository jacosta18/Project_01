# Four pillars of Object Oriented Programming
# Inheriatance

##### MOST FUNDAMENTAL POINT #####

class Vehicle():  ## super class of truck

    def __init__(self,make,color,engine_size,year,speed):
        self.make = make
        self.color = color
        self.engine_size = engine_size
        self.year = year
        self.speed = speed

    def start(self):
        return 'vroom'
    def stop(self):
        return 'screech'
    def accelerate(self):
        return self.speed ++10


class Truck(Vehicle): ## sub class of vehicle

    def __init__(self,make,color,engine_size,year,speed,trailer_size):
        super().__init__(make,color,engine_size,year,speed)  ## the super class is the parent class.
        self.trailer_size = trailer_size

class Boat(Vehicle): # Sub class of Truck

    def __init__(self,make,color,engine_size,year,speed, sails, anchor, deck):
        super().__init__(make,color,engine_size,year,speed)
        self.sails = sails
        self.anchor = anchor
        self.deck = deck

    def sink(self):
        return "siinking"


my_car = Vehicle('Honda','Red',1.6,1995,20)
my_truck = Truck("Ford","Silver",7.5,2019,14,10)
my_boat = Boat("Bertram","White",7.4,2016, 35,"large","huge","deck")

print(my_truck.start())

print(my_truck.accelerate())

print(my_truck.stop())

print(my_boat.sink())

print(f"Daniel has a {my_truck.make} of size {my_truck.engine_size} of color {my_truck.color} is {my_truck.year} old with a trailer {my_truck.trailer_size} long with a speed of {my_truck.speed}")
print(f"Daniel has a {my_car.make} of size {my_car.engine_size} of color {my_car.color} is {my_car.year} old with a speed of {my_car.speed}")
print(f"Daniel has a {my_boat.make} of size {my_boat.engine_size} of color {my_boat.color} is {my_boat.year} , a with a speed of {my_boat.speed} with a {my_boat.sails} sail and a {my_boat.anchor} anchor but a small {my_boat.deck}")







