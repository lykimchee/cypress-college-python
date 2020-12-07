from Date import *
from Event import *


events = []


def add_event():
    user_event_date = Date()

    while True:
        year = input("In what year will your event take place? ")
        if year.isdigit() and int(year) >= 2020:
            year = int(year)
            break
        else:
            print("The event must take place during or after the year 2020.")

    while True:
        month = input("In what month will your event take place? ")
        if month.isdigit() and 1 <= int(month) <= 12:
            month = int(month)
            break
        else:
            print("Please enter a valid month.")

    while True:
        day = input("On what day of the month will your event take place? ")
        if day.isdigit() and 1 <= int(day) <= 31:
            day = int(day)
            break
        else:
            print("Please enter a valid day.")

    Date.set_date(user_event_date, day, month, year)

    while True:
        user_start_time = input("What time does your event begin? ")
        if user_start_time.isdigit() and 0 <= int(user_start_time) <= 23:
            user_start_time = int(user_start_time)
            break
        else:
            print("Please enter a valid time in 24-hour format.")

    for i in events:
        if i.event_date == user_event_date:
            if i.start_hour < user_start_time < i.end_hour:
                print("An overlapping event already exists:")
                print(i)
                return

    while True:
        user_end_time = input("What time does your event end? ")
        if user_end_time.isdigit() and 0 <= int(user_end_time) <= 23:
            user_end_time = int(user_end_time)
            if user_end_time > user_start_time:
                break
            else:
                print("The ending time must be after the starting time.")
        else:
            print("Please enter a valid time in 24-hour format.")

    user_event_name = input("What is the name of your event? ")
    user_event = Event(user_event_name, user_start_time, user_end_time, user_event_date)
    events.append(user_event)
    print("Event successfully scheduled.")


def cancel_event():
    print("Please enter the name of the event you would like to cancel.")
    print("Note: Event names are case-sensitive.")
    user_event = input("Event name: ")
    for i in events:
        if i.event_name == user_event:
            events.remove(i)
            print("Event successfully canceled.")
            return
    print("No such event had been scheduled.")


def view_events():
    if len(events) == 0:
        print("There are currently no events scheduled.")
    for i in events:
        print(i)


def main():
    while True:
        print("\nType \"add\" to add a new event.")
        print("Type \"cancel\" to cancel an existing event.")
        print("Type \"view\" to view all scheduled events.")
        print("Type \"quit\" to quit.\n")
        user_input = input("Please enter an option: ")
        if user_input == "quit":
            break
        elif user_input == "add":
            add_event()
        elif user_input == "cancel":
            cancel_event()
        elif user_input == "view":
            view_events()
        else:
            print("Please enter a valid option.")


main()
