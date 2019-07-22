from Airport_Project.People import *
from Airport_Project.Airport_Inheriatance import *
from Airport_Project.Flights_airport import *
from Airport_Project.Using_Abstraction_Airport import *

trent_1000 = Jet_engine("Rolls Royce", "Trent", "Super big","Hydrogen Propelled")
A380 = Aircraft(trent_1000, "AirBus", "Black") # has a relationship

print(A380.engine.model)
# Abstraction ()
