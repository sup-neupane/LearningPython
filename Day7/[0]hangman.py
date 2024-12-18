import random

import hangmanWords 
import hangmanArt


print(hangmanArt.logo)

chosen_word = random.choice(hangmanWords.word_list)

lives = 6
display = []

word_length = len(chosen_word)


for _ in range(word_length):    #You can also wite for x in range(len(chosen_word)): but we arent doing anything with x so _
    display.append("_")

end_of_game = False

while not end_of_game:
    guess = input("Guess a word: ").lower()

    if guess in display:
        print(f"You have already Guessed the letter {guess}")

    for position in range(word_length):
        char = chosen_word[position]
        if char == guess:
            display[position] = char
    
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not a letter in the word!")
        if lives == 0:
            end_of_game = True
            print("You Loose!")
        

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print(hangmanArt.stages[lives])




