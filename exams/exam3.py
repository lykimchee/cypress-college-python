inventory = {}
# { 'flowers for algernon': 1, 'pride and prejudice': 4 }


def add_book():
    user_book = input("What book would you like to add? ")
    user_book = user_book.lower()
    if user_book not in inventory:
        inventory[user_book] = 1
    else:
        inventory[user_book] += 1
    print("Book successfully added!\n")


def find_book():
    user_book = input("What book would you like to find? ")
    user_book = user_book.lower()
    if user_book in inventory:
        print("There are " + str(inventory[user_book]) + " copies in stock.\n")
    else:
        print("Sorry, there are no copies in stock.\n")


def remove_book():
    user_book = input("What book would you like to remove? ")
    user_book = user_book.lower()
    if user_book in inventory:
        if inventory[user_book] > 1:
            inventory[user_book] -= 1
        else:
            del inventory[user_book]
        print("Your book was successfully removed.\n")
    else:
        print("The book does not exist in our inventory.\n")


def write_to_file():
    with open("books_inventory.txt", "w") as file:
        for title in inventory:
            file.write(title + str(inventory[title]) + "\n")


def load_data():
    with open("books_inventory.txt", "r") as file:
        for line in file:
            line = line.strip()
            title = line[:-1]
            stock = line[-1]
            inventory[title] = int(stock)


def main():
    try:
        load_data()
    except FileNotFoundError:
        pass

    print("Hello!")
    while True:
        print("Type \"q\" to quit,")
        print("\"add\" to add a new book,")
        print("\"find\" to find a book, or")
        print("\"remove\" to remove a book.")
        user_input = input("Enter an option: ")
        user_input = user_input.lower()

        if user_input == "q":
            write_to_file()
            break
        elif user_input == "add":
            add_book()
        elif user_input == "find":
            find_book()
        elif user_input == "remove":
            remove_book()
        else:
            print("That was not an option!\n")


main()
