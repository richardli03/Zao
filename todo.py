#accessing the calendar

import csv
def todo():
    with open("todo.csv", "r") as file:
        csv_reader = (csv.reader(file))
        next(csv_reader)
        todoList = list(csv_reader)
        
    return todoList

if __name__ == "__main__":
    print("\n")
    print("This is your current todo list: ")

    for task in todo():
        print (task[0],task[1])

   #print(*todo(), sep = "\n")

