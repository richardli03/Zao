#this will be displayed every time the user opens the terminal

from greet import *
from weather import *
from todo import *

from datetime import *

def main():
    current_time = datetime.now().strftime("%A %d, %B, %I:%M:%S %p")

    # greeting
    print("Hello, Richard! \n")
    print(greeting()[0])
    print("from: " + greeting()[1])   
    print("\n")

    # current time
    
    print("It is currently", current_time)
    print("\n")

if __name__ == "__main__":
    main()
            

 
