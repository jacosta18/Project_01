from Airport_Project.Airport_Inheriatance import Airplanes

class Fighter_plane(Airplanes):
    def __init__(self, engine, model, colour, plane_number, company,guns, missiles,speed):
        super().__init__(engine,model,colour,plane_number,company)
        self.guns = guns
        self.missiles = missiles
        self.speed = speed

    def break_sound_barrier(self):
        return self.speed ++ 305

    def can_roll(self, bool_value):
        return bool_value

    def can_fly_upside_down(self):
        return "They see me rolling"

fighter_plane = Fighter_plane("Turbo Jet","Typhoon","Grey / White","FZ-40","RAF","50 calibre","3 tonnes",0)

print(f"This airport has a fighter plane with a {fighter_plane.engine} engine made by {fighter_plane.model}. It comes in {fighter_plane.colour} and a plane number {fighter_plane.plane_number} run by a company called {fighter_plane.company}. It equips a {fighter_plane.guns} machine gun and {fighter_plane.missiles} worth of missiles. It can also break the sound barrier if goes {fighter_plane.break_sound_barrier()} mph faster than its average speed of 503mph")


print(fighter_plane.can_fly_upside_down())
print(fighter_plane.can_roll(True))

