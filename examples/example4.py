def main():
    largest = 0
    smallest = 0
    num_entered = False
    while True:
        num = int(input("Enter a number: "))
        if num == -99:
            break

        if not num_entered:
            num_entered = True
            smallest = num
            largest = num

        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

    if not num_entered:
        print("You entered no numbers.")
    else:
        print("The largest value is", largest, "and the smallest is", smallest)


main()
