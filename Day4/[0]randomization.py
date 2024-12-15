# Mersenne Twister is a pserdo-random number generator that is widely used in practice. It is the default random number generator in Python.
import random

random_integer = random.randint(1, 10)
#This generates random integer between 1 and 10 including 1 and 10
print(random_integer)

#For random float number
random_float = random.random() #This generated float number between [0,1) i.e. 0.00000000... to 0.9999999....
print(random_float)



# In Python's random module, seed() is used to initialize the random number generator. 
# A random number generator produces a sequence of numbers that appear random, but are 
# actually determined by an initial value called the "seed."

# Default Behavior (No Seed): If you don't set a seed, Python uses the system time or other system state 
# to initialize the random number generator, so you get different random sequences each time.

# Setting a Seed: When you set a specific seed using random.seed(x), the random number generator 
# will produce the same sequence of numbers every time the program is run with that seed.



#Virtual coin toss program
test_seed = int( input("Create a seed number:") )
random.seed(test_seed)

random_side = random.randint(0,1)

if random_side == 1:
    print("Head")
else:
    print("Tails")