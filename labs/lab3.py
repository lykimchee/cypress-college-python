def main():
    name = input("Enter your name: ")
    print("Welcome, " + name + "!")
    num1 = input("Enter a number: ")
    num2 = input("Now enter another: ")
    if num1.isdigit() and num2.isdigit():
        print("When you add " + num1 + " and " + num2 + ", the sum is...")
        print(int(num1) + int(num2))
        print("When you multiply " + num1 + " and " + num2 + ", the product is...")
        print(int(num1) * int(num2))
    else:
        print("That's not a number!")


main()
