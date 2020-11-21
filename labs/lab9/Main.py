from FullName import *


def main():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    your_name = FullName(last_name, first_name)
    print("Your name is " + str(your_name) + "!\n")

    # String is greater than the other if it comes later alphabetically
    my_name = FullName("kim", "lynn")
    if your_name < my_name:
        print("Your name comes alphabetically before " + str(my_name) + ".")
    elif your_name == my_name:
        print("You have the same name as " + str(my_name) + ".")
    else:
        print("Your name comes alphabetically after " + str(my_name) + ".")


main()
