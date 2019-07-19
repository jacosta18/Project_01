

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

class Aairplanes(Aircraft):

    def __init__(self, engine, model, colour,plane_number,company):
        super().__init__(engine, model, colour)
        self.plane_number= plane_number
        self.company = company

class Helicopters (Aircraft):
    def __init__(self,engine, model, colour,rudder):
        super().__init__(engine,model,colour)
        self.rudder = rudder


