
sound_factors = {
        3:"Pling",
        5:"Plang",
        7:"Plong",
}

def convert(sounds):
    if sounds in sound_factors:
        print("%s!" % sound_factors[sounds])
    else:
        print("Nope")

num=int(input("Enter number here: "))
convert(num)







