#defining a greeting function
#ideally will draw upon a random database to find compliments every single day 
import random
import csv

def greeting():
    print("Good morning, Richard!")

    #produce a random compliment
    key=(random.randrange(1, 3))

    #opening the CSV file containing all the compliments
    with open("compliments.csv", "r") as file:
        reader = csv.reader(file)

        #defining a counter that will find the key's row, returning that compliment
        row_counter = 0
        for n in reader:
            if row_counter == key:
                cell = n[1]
                print (cell)
            row_counter += 1        
      

