from Date import *
from Event import *


def main():
    event_info = []
    user_input = 0
    while user_input != 'q':
        user_input = input("Enter 1 to add an event, 2 to cancel an event, and 3 to view an event, and q to quit: ")

        if user_input.isdigit() and int(user_input) == 1:
            event_month = int(input("Which month is the event taking place? "))
            event_day = int(input("Which day is the event taking place? "))
            event_year = int(input("Which year is the event taking place? "))
            Date_object = Date(event_month, event_day, event_year)
            event_start_time = int(input("When is the event starting? "))
            event_end_time = int(input("When is the event ending? "))
            if event_start_time > event_end_time:
                print("Event start time must be before end time")
            event_name = input("What is the name of the event? ")
            Event_object = Event(event_name, event_start_time, event_end_time, Date_object)
            for i in event_info:
                if Event_object.event_date == i.event_date and Event_object.start_hour < i.end_hour:
                    print("An event already exists for this given day and time, the program will not add this event")
                    break
            event_info.append(Event_object)

        elif user_input.isdigit() and int(user_input) == 2:
            event_remove = input("Enter an event to remove: ")
            for i in range(len(event_info)):
                if event_info[i].name == event_remove:
                    del event_info[i]

        elif user_input.isdigit() and int(user_input) == 3:
            for Event_object in event_info:
                print(Event_object)

        if user_input == 'q':
            break


main()
