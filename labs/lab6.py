employees = {}


def lookup_employee(i):
    if i in employees:
        print("Your employee is " + employees[i] + ".")
    else:
        print("Employee not found.")


def main():
    with open("data//employees.txt") as file:
        for employee in file:
            num, first, last = employee.split()
            employees[num] = first + " " + last
        while True:
            i = input("Enter an employee ID: ")
            if i.isdigit():
                lookup_employee(i)
                break
            else:
                print("Please enter a number.")


main()
