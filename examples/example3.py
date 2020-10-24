def main():
    num_list = []
    while True:
        num = int(input("Enter a number: "))
        if num == -99:
            break
        num_list.append(num)
    num_list.sort()
    if len(num_list) == 0:
        print("You entered no numbers!")
    else:
        print("Smallest value is", num_list[0], "and largest value is", num_list[-1])


main()
