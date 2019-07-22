
class Aircraft():
    def __init__(self, engine, model, colour): # Use association to turn engine to an object
        self.engine = engine
        self.model = model
        self.colour = colour

    def can_take_off(self):
        return 'swoooshhh'

    def can_land(self):
        return 'screeeech'

    def can_crash(self):
        return 'AAAAAAHHHH'

class Engine():
    def __init__(self,make,model,size):
        self.make = make
        self.model = model
        self.size = size

class Jet_engine (Engine):
    def __init__(self,make,model,size, proportion_type):
        super().__init__(make,model,size)
        self.proportion_type = proportion_type


class Helicopter(Aircraft):
    def __init__(self,engine, model, colour,rudder):
        super().__init__(engine,model,colour)
        self.rudder = rudder

class Airplane(Aircraft):

    def __init__(self, engine, model, colour, plane_number, company):
        super().__init__(engine, model, colour)
        self.plane_number = plane_number
        self.company = company

#
# airplanes = Airplane("GE90-115B", "Airbus A380-800","white","ESA-1092","Antonov")
# helicopters = Helicopter("Turbo-Mecca Airrus", "G-Pola","black", "small")

# prias a helicopter with a {helicopters.engine} engine made by {helicopters.model}. It comes in {helicopters.colour} and a {helicopters.rudder} rudder at the back.")nt(airplanes.can_take_off())
# print(airplanes.can_crash())
# print(airplanes.can_land())
#
# print(f"This airport has an aeroplane with a {airplanes.engine} engine made by {airplanes.model}. It comes in {airplanes.colour} and a plane number {airplanes.plane_number} run by a company called {airplanes.company}.")
# print(f"This airport h