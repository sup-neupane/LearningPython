import higherLowerArt
import higherLowerData
import random
import os


#Generate a random person from data:
def generate():
    """Get data from random account"""
    return random.choice(higherLowerData.data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(personA_followers, personB_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if personA_followers > personB_followers:
    return "a"
  else:
    return "b"

def game():
    score = 0
    print(higherLowerArt.logo)
    #Generate random person A:
    personA = generate()
    #Generate random person B:
    personB = generate()
    game_should_continue = True

    while game_should_continue:
        personA = personB
        personB = generate()

        print(f"Compare A: {format_data(personA)}")

        print(higherLowerArt.vs)

        print(f"Against B: {format_data(personB)}")

        guess = input('Enter who has more followers? Type "A" or "B"').lower()

        os.system('cls')
        print(higherLowerArt.logo)
        if guess == check_answer( personA["follower_count"],personB["follower_count"]):
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()

   




