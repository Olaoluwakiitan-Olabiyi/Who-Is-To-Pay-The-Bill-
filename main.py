
import random

name_string= input("Enter everybody's name, separated by a comma.")
names=name_string.split(",")

print ("names")

number_names=len(names)

choice= random.randint (0, (number_names-1))

print (names[choice] +" is to pay for our meal today.")
    


