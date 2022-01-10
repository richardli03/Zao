import sys
import csv

# total arguments

def add(newTodoString):
    with open("todo.csv", "a") as file:
        writer = csv.writer(file)

        #NOTE: you have to put "newTodoString" in brackets because otherwise the writer treats it like a sequence of characters.
        writer.writerow([newTodoString])
    return True

if __name__ == "__main__":
    try: 
        sys.argv[2]
    except IndexError:
        print("Please type something to add to your to-do list!")
        exit()  

    command = '';  
    for arg in sys.argv[2:]:          # skip sys.argv[0] since the question didn't ask for it
        if ' ' in arg:
            command+= '"{}" '.format(arg) ;   # Put the quotes back in
        else:
            command+="{} ".format(arg) ;      # Assume no space => no quotes

    newTodoString = str(command.replace('"', ""))

    if add(newTodoString) == True:
        print(str(sys.argv[2:]) + " has been added to your todo list")
    else: 
        print("Sorry! There was an error adding this item to your todo")