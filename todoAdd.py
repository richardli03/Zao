import sys
import csv


def add(newTodo):

    
    with open("todo.csv", "r") as f:
        reader = csv.reader(f)
        length = len(list(reader))
        #print(length)
    f.close()
    
    headers = ['index','task']  
    newTask={'index': (length) ,'task': (newTodo)}
    
    with open("todo.csv", "a", newline ='') as f:
        dictwriter = csv.DictWriter(f, fieldnames=headers)
        dictwriter.writerow(newTask)
    f.close()
        
    return True


if __name__ == "__main__":
    
    # the task will be the 3rd thing entered from the command line (todoAdd.py add ...) 
    # we check if it exists
    try: 
        sys.argv[2]
    except IndexError:
        print("Please type something to add to your to-do list!")
        sys.exit()
    
     # we check to make sure task doesn't start with number (confuses todoFin)

    try: 
        isNumber = isinstance(int(sys.argv[2]),int)
        print("Please don't start your task with a number")
        sys.exit()
    except ValueError:
    # allows apostrophes if the task is in quotes 
        command = '';  
        for arg in sys.argv[2:]:          
            if ' ' in arg:
                command+= '"{}" '.format(arg) ;   # Put the quotes back in
            else:
                command+="{} ".format(arg) ;      # Assume no space => no quotes

        newTodo = str(command.replace('"', ""))

        if add(newTodo) == True:
            print(str([newTodo]) + " has been added to your todo list")
        else: 
            print("Sorry! There was an error adding this task to your todo")