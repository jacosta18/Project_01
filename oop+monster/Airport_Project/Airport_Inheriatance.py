

class Aircraft():
    def __init__(self, engine, model, colour):
        self.engine = engine
        self.model = model
        self.colour = colour

    def can_take_off(self):
        return 'swoooshhh'

    def can_land(self):
        return 'screeeech'

    def can_crash(self):
        return 'aaaaaaahhh'

class Helicopters (Aircraft):
    def __init__(self,engine, model, colour,rudder):
        super().__init__(engine,model,colour)
        self.rudder = rudder

class Airplanes(Aircraft):

    def __init__(self, engine, model, colour, plane_number, company):
        super().__init__(engine, model, colour)
        self.plane_number = plane_number
        self.company = company


airplanes = Airplanes("GE90-115B", "Airbus A380-800","white","ESA-1092","Antonov")
helicopters = Helicopters("Turbo-Mecca Airrus", "G-Pola","black", "small")

print(airplanes.can_take_off())
print(airplanes.can_crash())
print(airplanes.can_land())

print(f"This airport has an aeroplane with a {airplanes.engine} engine made by {airplanes.model}. It comes in {airplanes.colour} and a plane number {airplanes.plane_number} run by a company called {airplanes.company}.")
print(f"This airport has a helicopter with a {helicopters.engine} engine made by {helicopters.model}. It comes in {helicopters.colour} and a {helicopters.rudder} rudder at the back.")