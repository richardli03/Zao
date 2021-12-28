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
    greeting()
    print("\n")

    # current time
    current_time = datetime.now().strftime("%A %d, %B, %I:%M:%S %p")
    print("It is currently", current_time)
    print("\n")

    # current weather at this location
    print("Here's the weather for today:")
    weatherCheck()
    print("\n")

    #print("Here's what you need to do today")
    #todo()
    #print("\n") 

    #print("Would you like to tell me how you're doing?")
    #moodCheck() 

if __name__ == "__main__":
    main()
            

 
