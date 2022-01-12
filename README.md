# Zao 

---

A terminal assistant!

Zao is technically a bash script, but since I didn't want to write in bash, I just have that script calling different python files. Zao is capable of the following:

1. Saying hello every time you open the terminal with a random compliment!
2. Telling you the weather and temperature with a command
3. Adding things to a todo list, displaying that todo list, and removing things from that todo list.

### Usage

When you first install this package, it's important that you do the following

    ./Zao set name = [_insert your name here_]
    ./Zao set city_name = [_insert your city name here_]
    ./Zao set standard = metric OR imperial

This will allow Zao to figure out how best to display information to you!

---

Zao is a bash script with 5 functions:

    ./Zao                               
    This function will greet you! (note that this will run automatically on every new terminal instance)

    ./Zao weather                       
    This function will give you the weather

    ./Zao todo                          
    This function will display your todo list 

    ./Zao add [text]                    
    This function will add that item to your todo list at the next index.

    ./Zao fin [index number] OR [text]        
    This function will remove the item at that index on your todo list
    OR
    This function will find the closest approximate item on your todo list (according to the text you've entered) and ask you if that's what you want to remove.

#### Specifics:

The todo functionality in this code is a little bit finicky. Because you're able to remove things from your todo list with either an index or a word, the code can't let you start your todo task with a number. Don't worry, if you forget, the code will remind you!

Also if you want to type apostrophes ('), then you'll have to put your task in quotes. 

##### For example:
"Don't be scared to try new things" **works.**
Don't be scared to try new things **doesn't.**

In fact, the terminal will interpret this as a quote, so you won't even be able to input it into the program. 


### Dependencies:
1. requests
2. json
3. random
4. csv

### Learning goals:
1. Installing modules + coding in python
2. Good code hygiene and organization
3. Manipulating data (in this case, csv files)
