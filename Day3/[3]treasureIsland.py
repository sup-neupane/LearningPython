print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# You may have noticed the multi block string is inside ''' string '''
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")




option1 =  input('You\'re at a cross-road. Do u want to go "Left" or "Right"?').lower()
# In above statement the \ ignores ' in You're so that it dosent indicate end of string
if option1 == "left":
    option2 = input("Do you want to Swim or Wait? ").lower()
    if option2 == "wait":
        option3 = input("Which door? Red, Yellow or Blue? ").lower()
        if option3 == "yellow":
            print("You Found The Treasure!")
        elif option3 == "red":
            print("You got burnt in fire! Game over!")
        elif option3 == "blue":
            print("You fell from the sky! Game over!")
        else:
            print("Invalid Door! Game over!")
    else:
        print(("Sharks ate you! Game over!"))    
    
else:
    print("You fell into a hole! Game Over!")