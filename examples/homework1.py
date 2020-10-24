def ask_for_cards():
    while True:
        number = input("How many cards do you have? ")
        if number.isdigit():
            number = int(number)
            if 2 <= number <= 5:
                break
    return number


def ask_card_values(x):
    result = []
    count = 1
    while count < x+1:
        user_card = input("What is the value of card " + str(count) + "? ")
        result.append(user_card)
        count += 1
    return result


def calculate_total(li):
    ace_count = 0
    total = 0
    for i in li:
        if i.isdigit():
            total += int(i)
        elif i.lower() == "j" or i.lower() == "q" or i.lower() == "k":
            total += 10
        else:
            ace_count += 1

    if ace_count != 0:
        while ace_count > 0:
            if total + 10 <= 21:
                total += 10
            else:
                total += 1
            ace_count -= 1

    return total


def main():
    cards = ask_for_cards()
    deck = ask_card_values(cards)
    total = calculate_total(deck)
    if total > 21:
        print("You busted!")
    elif total == 21:
        print("Blackjack!")
    else:
        print("Your score was " + str(total) + ".")


main()
