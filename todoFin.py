from re import X
import sys
import csv
from todoAdd import isNumber

# total arguments
# may be helpful: https://stackoverflow.com/questions/66383841/how-to-write-on-nth-row-in-csv-using-python


def find(input):  
    found = False
    foundTask = []

    with open('todo.csv', 'r') as rf:
        reader = csv.reader(rf)

        if isNumber(input) == True:
            index = input
            for row in reader:
                if row[0] == index:
                    # print("row[0]: ")
                    # print(row[0])
                    # print(row[1])
                    foundTask.append(row)
                    found = True
        else:
            task = input 
            for row in reader:     
                if task.lower() in row[1].lower():
                    # print("row[1]: ")
                    print(row[1])
                    foundTask.append(row)
                    found = True
    rf.close()

    if found == False:
        # print("task not found!")
        return False
    else:
        # print("task found!")
        return foundTask

def validation(task):
    readyCheck = False
    while True:
        yesNo = input("Are you sure you want to finish this task? (y/n) ")
        if yesNo.lower() == "yes" or yesNo.lower() == "y":
            readyCheck = True
            break 
        elif yesNo.lower() == "no" or yesNo.lower() == "n":
            readyCheck = False
            break
        else:
            print("please enter yes, no, y, or n")
    
    return readyCheck

def finish(task):

    # this code deletes the row in the csv file connected to a certain task name
    lines = list()
    delCheck = 0

    with open('todo.csv', 'r') as rf:
        reader = csv.reader(rf)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == task:
                    lines.remove(row)
                    delCheck = 1
    rf.close()

    if delCheck == 0:
        return False
    else:
        with open('todo.csv', 'w') as wf:
            writer = csv.writer(wf)
            writer.writerows(lines)
        wf.close()
        return True

if __name__ == "__main__":
    
    # checking to make sure there is a task to remove
    try: 
        task = sys.argv[2]   
    except IndexError:
        print("Please type something to finish off your todo list")
        sys.exit() 

    findTask = find(task)

    if findTask == False:
        print("Sorry, we couldn't find a task matching your input.")
        sys.exit()
    
    print("We found the following tasks match your input: ")
    print(findTask)
    
    if len(findTask) > 1:
        choice = input("which task would you like to delete? please enter the number! ")
        findTask = find(choice)
        print(findTask)
    
    readyCheck = validation(task)

    if readyCheck == False:
        print("Good luck finishing that task! ")
        sys.exit()

    print("this task will be deleted")
    print(findTask)

    finishTask = finish(findTask[0][1])

    if finishTask == True:
        print(str([findTask]) + " has been finished. Good job! :)")
    else: 
        print("Sorry! There was an error finishing this task") 
    
        



    
   

        
    