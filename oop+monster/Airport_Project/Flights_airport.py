

class Flight():

    def __init__(self, plane, passengers_list,destination,origin):
        self.plane = plane
        self.passengers_list = passengers_list
        self.destination = destination
        self.origin = origin

    def cancelled(self):
        return "Your flight has been cancelled!"

    def delayed(self):
        return "Flight has been delayed due to poor weather conditions!"


#
# flight_01 = Flight("Emirates",234,"Singapore","London Heathrow")
# #flight_02 = Flight()


#
# print(flight_01.cancelled())
# print(flight_01.delayed())
#
#
# print(f"The next Flight with {flight_01.plane} has a manifest of {flight_01.passengers_list} passengers going to {flight_01.destination} from {flight_01.origin}.")