#run this file!

from greet import *
from weather import *
from todo import *
from mood import *

from datetime import *

def main():

    print("\n")

    # greeting
    print("Good morning, Richard!")
    print(greeting())   
    print("\n")

    # current time
    current_time = datetime.now().strftime("%A %d, %B, %I:%M:%S %p")
    print("It is currently", current_time)
    print("\n")

if __name__ == "__main__":
    main()
            

 
