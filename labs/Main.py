from Dice import *


def main():
    list_of_dice = []
    # ADD DICE OBJECTS
    for i in range(5):
        list_of_dice.append(Dice())
    # ROLL EACH DICE
    for i in list_of_dice:
        i.roll()
    # PRINT CUR_SIDE FOR EACH
    for i in list_of_dice:
        print(i.cur_side)


main()
