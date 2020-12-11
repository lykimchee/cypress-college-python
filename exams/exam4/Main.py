from Question import *


def main():
    player_one_score = 0
    player_two_score = 0
    questions = []

    question_one = Question("What is the capital of California?",
                            "San Diego",
                            "Sacramento",
                            "Los Angeles",
                            "San Francisco",
                            2)
    question_two = Question("What school is not in Anaheim Union High School District?",
                            "Oxford Academy",
                            "Cypress High School",
                            "Lexington Junior High",
                            "Sunny Hills High School",
                            4)
    question_three = Question("In what month does Christmas take place?",
                              "February",
                              "August",
                              "October",
                              "December",
                              4)
    question_four = Question("Which of the following is not an AP class?",
                             "Calculus",
                             "Chinese",
                             "Korean",
                             "Physics",
                             3)
    questions.append(question_one)
    questions.append(question_two)
    questions.append(question_three)
    questions.append(question_four)

    # PLAYER INTERACTION
    for i in questions:
        player_one_flag = False
        player_two_flag = False
        print(i)

        while True:
            input_one = input("Player one, your guess? ")
            if input_one.isdigit() and 1 <= int(input_one) <= 4:
                input_one = int(input_one)
                break
            else:
                print("Please enter a valid number between 1 to 4.")
        if i.guess(input_one):
            player_one_score += 1
            player_one_flag = True
        print("Player one answer recorded.\n")

        while True:
            input_two = input("Player two, your guess? ")
            if input_two.isdigit() and 1 <= int(input_two) <= 4:
                input_two = int(input_two)
                break
            else:
                print("Please enter a valid number between 1 to 4.")
        if i.guess(input_two):
            player_two_score += 1
            player_two_flag = True
        print("Player two answer recorded.\n")

        print("The correct answer was " + i.answer_string() + ".")
        if player_one_flag and player_two_flag:
            print("Both players got this question correct.\n")
        else:
            if player_one_flag:
                print("Player one got this question correct.\n")
            elif player_two_flag:
                print("Player two got this question correct.\n")
            else:
                print("No players got this question correct.\n")

    # END OF QUESTIONS
    print("Player one's score is: " + str(player_one_score) + ".")
    print("Player two's score is: " + str(player_two_score) + ".")
    if player_one_score > player_two_score:
        print("Player one wins!")
    elif player_one_score < player_two_score:
        print("Player two wins!")
    else:
        print("It's a draw!")


main()
