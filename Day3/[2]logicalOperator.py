#Logical operators:
# and --> and
# or --> or
# not -->not

# lower() this function turns to lowercase
# e.g. "Suparna".lower()  #This gives output as suparna

#count() this gives occurance of a character in a string
#e.g. "Suparna".count("a") This gives output 2
#Note "Suparna".count("a") this only gives occurance of lowercase a if capital A tehn dosent count

#Love Calulator
print("Welcome to love calculator")
name1 = input("What is your name?\n")
name2 = input("What is your name?\n")

combined_string = name1 + name2 
lower_combined_string = combined_string.lower()

t = lower_combined_string.count("t")
r = lower_combined_string.count("r")
u = lower_combined_string.count("u")
e = lower_combined_string.count("e")
true = t + r + u + e

l = lower_combined_string.count("l")
o = lower_combined_string.count("o")
v = lower_combined_string.count("v") 
e = lower_combined_string.count("e") 
love = l + o + v + e

love_score = int( str(true) + str(love) )

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is: {love_score}, you go together like coke and mentos!")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is: {love_score}, you are alright together!")
else:
    print(f"Your love score is: {love_score}")