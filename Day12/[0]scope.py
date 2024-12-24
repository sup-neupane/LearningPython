enemies = 1

def increase_enemies():
    enemies = 2
    print(f"The number of enemies inside function is {enemies}")  #This prints 2

increase_enemies()
print(f"The number of enemies outside function is {enemies}")    #This prints 1

#The above observation is due to scope

#Local Scope:
def drink_potion():
    potion_strength = 2
    print(f"The player health is {potion_strength}")  #This prints 2

drink_potion()
# print(f"The player health is {potion_strength}")   #This prints error as when we define a variable inside 
                                                 #function its scope is only inside that function

#Global Scope:
player_health = 10
def drink_potion():
    potion_strength = 2
    print(f"The player health is {player_health}")  #This prints 10

drink_potion()
print(f"The player health is {player_health}")   #This prints 10 as player strenghth is defines outside functions 
                                                #so it is available both inside and outside function



#This concept of global and local variables dosent only apply to variables but also to functions and anything that you can name
#This is the concept called namespace, anything you give a name to has a namespace and that namespace is valid in certain scopes

#Unlike most languages python dosent have a block scope e.g:
#If you create a new variable inside a if statement or while loop or for loop then the scope of that variable isnt
#inside that block(if statement, loop) as other languages it has scope as enclosing function or if it isnt inside any 
#function the variable has global scope





