# split(", ") This function allows to split a string to list based on seperator mentioned inside ""
import random

test_seed = int( input("Enter a seed: ") )
random.seed(test_seed)

name_as_csv = input('Enter everybodys name seperated by ",": ') 
names = name_as_csv.split(", ")

length = len(names) - 1
random_index = random.randint(0,length)

print(f"{names[random_index]} is going to pay the bill!")
