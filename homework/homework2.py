def view_scores():
    with open("scores.txt", "r") as file:
        file_text = file.read()
        if file_text != "":
            # THERE IS SCORE DATA IN THE SCORES.TXT FILE
            for line in file_text.splitlines():
                # PRINT A STATEMENT FOR EACH DATE/LINE
                row_as_a_list = line.split()
                month = row_as_a_list[0]
                day = row_as_a_list[1]
                print("On " + month[0].upper() + month[1:].lower() + " " + day + ", you scored", end=" ")
                # PRINTS THE SCORES AFTER MONTH AND DAY
                for score in range(2, len(row_as_a_list)-1):
                    print(row_as_a_list[score], end=", ")
                print("and " + row_as_a_list[len(row_as_a_list)-1] + ".")
            print()
        else:
            print("Sorry, there are no existing scores.\n")


def add_score():
    with open("scores.txt", "a") as file:
        # GETS MONTH AND DATE FROM USER
        user_month = input("Please enter a month: ")
        while True:
            user_day = input("Please enter a day: ")
            if user_day.isdigit() and 1 <= int(user_day) <= 31:
                break
            else:
                print("That's not a valid date!")

        # CHECKS IF SCORES EXIST FOR A DATE
        if score_exists_for_date(user_month, user_day):
            print("Scores already exist for this date!\n")
        else:
            # ADDS SCORE FOR NEW DATE
            file.write(user_month + " " + user_day + " ")
            # GETS NUMBER OF SCORES TO ADD + INPUT VALIDATION
            while True:
                number_of_scores = input("How many scores would you like to add? ")
                if number_of_scores.isdigit() and int(number_of_scores) > 0:
                    break
                else:
                    print("That's not a valid number!")
            for i in range(int(number_of_scores)):
                # INPUT VALIDATION FOR SCORES -> ADDS NEW SCORE
                while True:
                    new_score = input("Please enter a score: ")
                    if new_score.isdigit() and 0 <= int(new_score) <= 300:
                        file.write(new_score + " ")
                        break
                    else:
                        print("Please enter a score between 0 and 300.")
            file.write("\n")
            print("Score(s) successfully added.\n")


def score_exists_for_date(the_month, the_day):
    with open("scores.txt", "r") as file:
        for row in file:
            # PLACEHOLDERS TO PREVENT ERRORS DURING FIRST INSTANCE OF ADDING A SCORE
            m = "month placeholder"
            d = "day placeholder"
            m, d, *scores = row.split()
            if the_month.lower() == m.lower() and the_day == d:
                return True


def average_scores():
    score_sum = 0
    count = 0
    with open("scores.txt", "r") as file:
        scores_text = file.read()
        if scores_text != "":
            # THERE IS SCORE DATA IN THE SCORES.TXT FILE
            for line in scores_text.splitlines():
                # FOR EACH LINE/DATE IN SCORES.TXT CREATE LIST OF EVERY WORD/NUMBER
                row_as_list = line.split()
                # ADD EVERY SCORE TO SCORE_SUM USING LIST
                for i in range(2, len(row_as_list)):
                    score_sum += int(row_as_list[i])
                    count += 1
            average_val = score_sum / count
            print("Your average score was " + str(average_val) + ".\n")
        else:
            print("Sorry, there are no existing scores.\n")


def main():
    with open("scores.txt", "w"):
        while True:
            print("Hello!")
            print("Type \"q\" to quit,")
            print("\"view\" to view scores,")
            print("\"add\" to add a new score, or")
            print("\"avg\" to get the average.")
            user_input = input("Enter an option: ")
            user_input = user_input.lower()

            if user_input == "q":
                break
            elif user_input == "view":
                view_scores()
            elif user_input == "add":
                add_score()
            elif user_input == "avg":
                average_scores()
            else:
                print("That was not an option!\n")


main()
