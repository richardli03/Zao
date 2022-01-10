#accessing the calendar

import csv
def todo():
    with open("todo.csv", "r") as file:
        todoList = list(csv.reader(file))
    return todoList

if __name__ == "__main__":
    print("This is your current todo list: ")
    print(*todo(), sep = "\n")

