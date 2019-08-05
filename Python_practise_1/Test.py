
# The folowing function will be printing out the factors of x

def print_factors(x):
    print("The factors of" , x, "are:")

    for b in range(1, x + 1):
        if x% b == 0:           # Modulus is used to the placeholder b
            print(b, end=" ")   # End is introduced to print the variables horizontally.

    for b in range(1,x +1):

        if b == 3:
            print("Pling!")

        elif b == 5:
            print("Plong")

        elif b == 7:
            print("Plang")





num = int(input("Enter a number:"))

print_factors(num)