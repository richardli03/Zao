# defining a greeting function
# ideally will draw upon a random database to find compliments every single day 
import random
import csv

def greeting():
    # opening the CSV file containing all the compliments
    with open("compliments.csv", "r") as file:
        data = list(csv.reader(file))
        
    # defining a counter that will find the key's row, returning that compliment
    compliment = random.choice(data)
    #print(compliment[1])
    name = compliment[2]  
    #print out compliment
    author = name if name else ("anonymous")

    greet = [(compliment[1]), author]
    return greet
    
if __name__ == "__main__":
    greeting()

        
           
   

