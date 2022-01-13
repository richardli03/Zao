from re import X
import sys
import csv
from todoAdd import isNumber

# total arguments
# may be helpful: https://stackoverflow.com/questions/66383841/how-to-write-on-nth-row-in-csv-using-python


def find(input):  
    found = False
    with open('todo.csv', 'r') as rf:
        reader = csv.reader(rf)

        if isNumber(input) == True:
            index = input
            for row in reader:
                if row[0] == index:
                    # print("row[0]: ")
                    # print(row[0])
                    found = True
        else:
            task = input 
            for row in reader:     
                if task in row[1]:
                    # print("row[1]: ")
                    # print(row[1])
                    foundTask = line.append(row[1])
                    found = True
    rf.close()

    if found == False:
        # print("task not found!")
        return 
    else:
        # print("task found!")
        return True



#def finish(task):

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
    
    print("We found the following tasks match your input: ")


    # if the task is successfully finished
    if finish(task) == True:
        print(str([task]) + " has been finished. Good job! :)")
    else: 
        print("Sorry! There was an error finishing this task")
        
   

        
    