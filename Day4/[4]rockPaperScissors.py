# Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
response = [rock, paper, scissors]

user_choice = int( input("Welcome to Rock Paper and Scissors! Type 0 for Rock, 1 for paper and 2 for Scissors:\n ") )


print(response[user_choice])

computer_choice =  random.randint(0,2)
print(f"Computer Choose:\n " + response[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("Invalid Number! You Loose!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_choice == 2:
    print("You Loose!")
elif user_choice < computer_choice:
    print("You loose!")
elif user_choice>computer_choice:
    print("You Win!")
elif user_choice == computer_choice:
    print("It's a draw!")

