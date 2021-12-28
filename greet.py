# defining a greeting function
# ideally will draw upon a random database to find compliments every single day 
import random
import csv

def greeting():
    # produce a random compliment
    key=(random.randrange(1, 6))

    # opening the CSV file containing all the compliments
    with open("compliments.csv", "r") as file:
        reader = csv.reader(file)

        # defining a counter that will find the key's row, returning that compliment
        row_counter = 0
        for n in reader:
            if row_counter == key:
                print ("'" + n[1] + "'")
                # listing author name if it exists, otherwise listing anonymous 
                if not (n[2]):
                    print ("- anonymous")
                else:
                    print ("- " + n[2])
            row_counter += 1  
           
   

