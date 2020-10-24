def get_score(exam_no):
    while True:
        user_input = input("What was your grade on exam " + str(exam_no) + "? ")
        if int(user_input) < 0 or int(user_input) > 100:
            print("Please enter a valid score.")
        else:
            return int(user_input)


def main():
    score_sum = 0
    scores = []

    for i in range(1, 6):
        scores.append(get_score(i))

    for score in scores:
        score_sum += score

    print("Your average exam grade is " + str(score_sum/5) + ".")


main()
