sound_factors = {
        3: "Pling",
        5: "Plang",
        7: "Plong",
}

factors = (3, 5, 7)

def divisible (number, divisior):
    return number % divisior == 0

def raindrops(number):
    return [sound_factors[factors]
            for factors in factors
            if divisible(number, factors)]

print(raindrops(30))
print(type(raindrops(30)))
