def sales(x):
    x = str(x)
    while True:
        result = input("Enter today's sales for store " + x + ": ")
        if result.isdigit() is True and int(result) % 100 == 0:
            break
    return int(result)


def charts(x, y):
    stars = x / 100
    count = 0
    y = str(y)
    print("Store " + y + ": ", end='')
    while count < stars:
        print("*", end=''),
        count += 1
    print()


def main():
    store1 = sales(1)
    store2 = sales(2)
    store3 = sales(3)
    store4 = sales(4)
    store5 = sales(5)
    print("\nSALES BAR CHART")
    print("(Each * = $100)")
    charts(store1, 1)
    charts(store2, 2)
    charts(store3, 3)
    charts(store4, 4)
    charts(store5, 5)


main()
