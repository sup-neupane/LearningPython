import os
import blackJackArt
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    random_card = random.choice(cards)
    return random_card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21 and len(cards) == 2:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_cards(computer_score,player_score):
    if player_score > 21:
        print("Print you went over sorry")




def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose  😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent. has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "Yoe lose 😤"


def play_game():
    print(blackJackArt.logo)
    computer_cards = []
    player_cards = []
    is_Game_Over = False
    for _ in range(2):
        computer_cards.append(deal_card())
        player_cards.append(deal_card())
    while not is_Game_Over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(player_cards)

        print(f"   Your cards: {player_cards}, current score: {player_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_Game_Over = True
        else:
            if input("Do You Want To Draw a Card? Type 'y' for yes and 'n' for no").lower() == "y":
                player_cards.append(deal_card)
            else:
                is_Game_Over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {player_cards}, final score: {player_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))



while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    os.system('cls')
    play_game()

