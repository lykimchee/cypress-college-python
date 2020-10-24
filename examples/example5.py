def get_sales(div_num):
    sales = input("Enter the sales for division " + str(div_num) + ": ")
    return sales


def main():
    num_divs = input("How many divisions does your company have? ")
    sales = []
    for i in range(1, int(num_divs)+1):
        s = get_sales(i)
        sales.append(s)

    print()

    for i, sale in enumerate(sales):
        print("The sales for division " + str(i+1) + " were $" + sale)


main()
