# First step, lets use dictionaries to assign each factor with a string:

# Dict
sound_factors = {
        3: "Pling",
        5: "Plang",
        7: "Plong",
}

# Creating a list of the factors of interest.

factors = (3, 5, 7)

# While loops is introduced to make the fucntion interactive.

while True:

    # Adding an input allows the user to 'Enter a value'
    num = int(input("Enter a number here: "))

    # The following function is to confirm whether or not the number can be divided.
    def divisible (number, divisior):
        return number % divisior == 0

#print(divisible(35,5))

    # This function links the variable 'number' to the function above.
    #
    def raindrops(number):
        return [sound_factors[factors]
                for factors in factors
                if divisible(number, factors)]

#print(raindrops(40))

    def convert(number):
        say = raindrops(number)
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