
sound_factors = {
        3: "Pling",
        5: "Plang",
        7: "Plong",
}

factors = (3, 5, 7)


class Raindrops():
    def __init__(self,number,divisor):
        self.number = number
        self.divisor = divisor

    def divisible(number, divisior):
        return number % divisior == 0

    def sound_effect(number):
        return [sound_factors[factors]
                for factors in factors
                if divisible(number, factors)]

    def convert(number):
        speak = raidndrops(number)
        return " ".join(speak) if speak else str(number)



