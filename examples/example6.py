def main():

    file1 = set()
    file2 = set()

    with open("first_file.txt") as file:
        for word in file.read().lower().split():
            file1.add(word)

    with open("second_file.txt") as file:
        for word in file.read().lower().split():
            file2.add(word)

    both = file1.intersection(file2)
    print(both)


main()
