from Airport_Project.Airport import Airplanes

class Fighter_plane(Airplanes):
    def __init__(self, engine, model, colour, plane_number, company,guns, missles):
        super().__init__(engine,model,colour,plane_number,company)
        self.guns = guns
        self.missles = missles

        

