
while True:
    def convert(sounds):
        sound_factors = {
            3: "Pling",
            5: "Plang",
            7: "Plong",
    }
        if sounds in sound_factors:
            print("%s!" % sound_factors[sounds])
        # else:
        #     for i in range(1, sounds + 1):
        #         if sounds % i == 0:
        #             print(i)
    break

num=int(input("Enter number here: "))
convert(num)