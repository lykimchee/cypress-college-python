import random


def get_user_answer():
    while True:
        user_input = input("Guess the number I'm thinking of! Hint: It's between 1 and 100: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Oops, that's not a number!")


def main():
    answer = random.randint(1, 100)
    while True:
        user_answer = get_user_answer()
        if user_answer == answer:
            print("Congratulations, you guessed correctly!")
            break
        elif user_answer > answer:
            print("Your guess was too high. Try again!")
        else:
            print("Your guess was too low. Try again!")


main()
