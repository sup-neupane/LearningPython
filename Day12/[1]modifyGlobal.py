#Modifying global variable:
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"The number of enemies inside function is {enemies}")  #This prints 2

increase_enemies()
print(f"The number of enemies outside function is {enemies}")    #This prints 1

#This might look like we are updating global variable enemies inside function increase_enemies()
#but actually we are creating a new variable enemies inside the function 

#If we want to modify global variable then we must do as:


enemies = 1

def increase_enemies():
    global enemies 
    enemies = 2
    print(f"The number of enemies inside function is {enemies}")  #This prints 2

increase_enemies()
print(f"The number of enemies outside function is {enemies}")    #This prints 2

#Note: It is not good pratice to modify global variable inside a function