def convert(sounds):
    for i in range(1, sounds + 1):
        if sounds % i == 0:
            print(i)

            sound_factors = {
            3: "Pling",
            5: "Plang",
            7: "Plong",
    }
        if sounds in sound_factors:
            print("%s!" % sound_factors[sounds])



num = 6
convert(num)

# while True:
#     print('Welcome to the loop')
#     word = input('Tell me a word \n')
#     # break # -
#     if word == 'bananas':    # condition to go into the break key word
#         print('you cracked the code')
#         break    # Safe word to break the loop
#     else:
#         print("HAHAHAHAHA YOU FOOL. YOU WILL NEVER LEAVE")
#         print("AHAHAHA")






#
#
# num = int(input("Enter number here: "))
# convert(num)