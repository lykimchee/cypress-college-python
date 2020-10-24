import random


def main():
    num1 = random.randint(0, 999)
    num2 = random.randint(0, 999)
    user_answer = input(str(num1) + " + " + str(num2) + " = ")
    if not user_answer.isdigit():
        print("You didn't enter a number!")
    else:
        num_sum = num1 + num2
        if int(user_answer) == num_sum:
            print("Correct!")
        else:
            print("Sorry, the correct answer is " + str(num_sum) + ".")


main()
