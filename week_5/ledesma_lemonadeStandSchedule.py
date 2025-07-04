"""
Author:         Devin Ledesma
Date:           07/04/2025
File Name:      ledesma_lemonadeStandSchedule
Description:    This file demonstrates the use of creating and iterating over two lists with if...else statements to manage a weekly schedule for a lemonade stand.
"""

# List of tasks related to running a lemonade stand
tasks = [
    "Buy lemons and supplies",
    "Prep lemonade",
    "Go to the bank",
    "Count inventory",
    "Deep clean lemonade stand"
]

# Loop through tasks and print to the console
print("Weekly Tasks:")
for task in tasks: # loops through tasks list
    print(task) # prints each task on new line

# List of days of the week
days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

print(" ") # line break

# For loop to display weekly tasks assigned to each day of the week
print("Daily Tasks:")
for i, day in enumerate(days): # provides index for looping through days list
    if day == "Saturday" or day == "Sunday": # prints specialized message for Saturday and Sunday only
        print(f"{day}: We're Closed. Rest up and enjoy the day off!")
    else:
        print(f"{day}: {tasks[(i-1) % len(tasks)]}") # corrects the list order
