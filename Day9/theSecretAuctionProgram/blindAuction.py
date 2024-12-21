import os
import blindAuctionArt

print(blindAuctionArt.logo)

print("Welcome to the secret auction program")

bidders = {}

def declare_winner(bidders):
    highest_amount = 0
    for bidder in bidders:
        amount = bidders[bidder]
        winner = ""
        if amount > highest_amount:
            highest_amount = amount
            winner = bidder
    print(f"The winner is {winner} and they won with bid amount {highest_amount}")

end_of_game = False

while not end_of_game:
    name_of_bidder = input("What is your name ")
    bid_of_bidder = int(input("What is your Bid: $"))
    bidders[name_of_bidder] = bid_of_bidder 
    option = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if option == "no":
        end_of_game = True
        declare_winner(bidders)
    elif option == "yes":
        os.system('cls')