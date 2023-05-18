# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Daniel Medrano Figueroa,05/14/2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:
    objFile = open("ToDoList.txt", "r")
    for row in objFile:
        lstRow = row.split(",")
        dicRow = {"Task": lstRow[0].strip(), "Priority": lstRow[1].strip()}
        lstTable.append(dicRow)
    objFile.close()
except FileNotFoundError:
    print("ToDoList.txt not found. Creating a new file.")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice == '1':
        print("Current Data:")
        if len(lstTable) > 0:
            for row in lstTable:
                print("Task:", row["Task"], "\tPriority:", row["Priority"])
        else:
            print("No data found.")
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice == '2':
        task = input("Enter a new task: ")
        priority = input("Enter the priority for the task: ")
        dicRow = {"Task": task, "Priority": priority}
        lstTable.append(dicRow)
        print("Task added successfully!")
        continue

    # Step 5 - Remove a new item from the list/Table
    elif strChoice == '3':
        if len(lstTable) > 0:
            task = input("Enter the task to remove: ")
            found = False
            for row in lstTable:
                if row["Task"].lower() == task.lower():
                    lstTable.remove(row)
                    found = True
                    print("Task removed successfully!")
                    break
            if not found:
                print("Task not found.")
        else:
            print("No data found.")
        continue


