# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog :
# RRoot,1.1.2030,Created started script
# TWOLDEMICHAEL, 02.21.2020 completed scriot
# <Tomas Woldemichael>,<02.21.2020E>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
# TODO: Add Code Here

f = open("/Users/shooter/Documents/_PythonClass/Assignment05/ToDoToDoList.txt", 'r')
for row in f:
    #dicRow = {} is this need ? verify
    strData, strData1 = row.split(',')
    dicRow = {'task': strData, 'priority': strData1.strip()}
    lstTable.append(dicRow)
    #print(lstTable)

f.close()

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
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
           for row in lstTable:
               print(row['task'], '\t', row['priority'])
               continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        while True:
            dicRow = {}
            task = input('What is the task ')
            priority = input('What is the priority (low or high) ')
            dicRow['task'] = task
            dicRow['priority'] = priority
            lstTable.append(dicRow)
            #print(lstTable)
            choice = input('would you like to input another value (Y or N) ')
            if 'y' == choice.lower():
                continue
            else:
                break
        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
         #TODO: Add Code Here
         while True:
             strItem = input('Item to remove ')
             strStatus = 'Row not found'
             for row in lstTable:
                 if row['task'].lower() == strItem.lower():
                     lstTable.remove(row)
                     strStatus = 'Row Removed'

             print(strStatus)

             print('Current Data', lstTable)
             strChoice = input('Exit (y/n) ')
             if strChoice.lower() == 'y':
                 break
         continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        f = open(objFile, 'w')
        for row in lstTable:
           f.write(row['task'] + ',' + row['priority'] + '\n')

        f.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print('GOOD BYE')
        break  # and Exit the program
