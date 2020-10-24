def get_num_miles():
    while True:
        number_miles = input("How many miles did your car travel? ")
        if number_miles.lower() == "quit":
            return "quit"
            break
        elif number_miles.isdigit():
            break
        else:
            print("Please enter a valid number of miles!")
    return number_miles


def get_num_gallons():
    while True:
        number_gallons = input("How many gallons of gas did the car need? ")
        if number_gallons.lower() == "quit":
            return "quit"
            break
        elif number_gallons.isdigit():
            break
        else:
            print("Please enter a valid number of gallons!")
    return number_gallons


def calculate(x, y):
    return round(int(x)/int(y))


def main():
    while True:
        print("Type \"quit\" at any time to stop playing!")
        miles = get_num_miles()
        if miles == "quit":
            break
        gallons = get_num_gallons()
        if gallons == "quit":
            break
        print("Your car achieved approximately " + str(calculate(miles, gallons)) + " miles per gallon!")
        print()


main()
