import sys
import csv
import pandas 


def add(newTodoString):

    
    with open("todo.csv", "r") as f:
        reader = csv.reader(f)
        length = len(list(reader))
        print(length)
    f.close()
    
    headers = ['index','task']  
    newTask={'index': (length) ,'task': (newTodoString)}
    
    with open("todo.csv", "a", newline ='') as f:
        dictwriter = csv.DictWriter(f, fieldnames=headers)
        dictwriter.writerow(newTask)
    f.close()
        
    return True


if __name__ == "__main__":
    try: 
        sys.argv[2]
    except IndexError:
        print("Please type something to add to your to-do list!")
        exit()  

    command = '';  
    for arg in sys.argv[2:]:          
        if ' ' in arg:
            command+= '"{}" '.format(arg) ;   # Put the quotes back in
        else:
            command+="{} ".format(arg) ;      # Assume no space => no quotes

    newTodoString = str(command.replace('"', ""))

    if add(newTodoString) == True:
        print(str([newTodoString]) + " has been added to your todo list")
    else: 
        print("Sorry! There was an error adding this item to your todo")