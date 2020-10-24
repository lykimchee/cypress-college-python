def ask_for_number():
    while True:
        user_input = input("Enter a number: ")
        if user_input.isdigit():
            result = int(user_input)
            break
        else:
            print("Please enter a valid number.")
    return result


def go_again():
    while True:
        user_input = input("Calculate another sum? Type yes or no: ")
        if user_input.lower() == "yes":
            return True
        elif user_input.lower() == "no":
            return False
        else:
            print("Please enter yes or no.")


def main():
    while True:
        number1 = ask_for_number()
        number2 = ask_for_number()
        number_sum = number1 + number2
        with open("data//results.txt", "a") as file:
            file.write(str(number1) + " + " + str(number2) + " = " + str(number_sum) + "\n")
        print("The sum of " + str(number1) + " + " + str(number2) + " is " + str(number_sum) + ".")
        if not go_again():
            break


main()
