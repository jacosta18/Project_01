# First step, lets use dictionaries to assign each factor with a string:

sound_factors = {
        3: "Pling",
        5: "Plang",
        7: "Plong",
}

# Creating a list of the factors of interest.

factors = (3, 5, 7)


while True:

    num = int(input("Enter a number here: "))

    def divisible (number, divisior):
        return number % divisior == 0

#print(divisible(35,5))

    def raidndrops(number):
        return [sound_factors[factors]
                for factors in factors
                if divisible(number, factors)]

#print(raidndrops(40))

    def convert(number):
        say = raidndrops(number)
        return " ".join(say) if say else str(number)


    print(convert(num))

    word = input("Would you like to continue (yes/no)?")

    if word == 'no':

        print("Thank you, Goodbye!")
        break

    else:
        print("Welcome back!")


# num = int(input("Enter a number here: "))
#
# print(convert(num))



