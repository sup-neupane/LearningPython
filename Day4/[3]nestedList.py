# List of Dirty Dozen for 2024
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Peaches", "Pears", 
#                "Nectarines", "Apples", "Grapes", "Bell Peppers", 
#                "Cherries", "Blueberries", "Green Beans"]

# Above is the list of dirty dozen but it has both fruits and vegetables so we can use nested structure to better visualize them
# Dirty Dozen for 2024 separated into fruits and vegetables
fruits = ["Strawberries", "Peaches", "Pears", "Nectarines", 
          "Apples", "Grapes", "Cherries", "Blueberries"]

vegetables = ["Spinach", "Kale", "Bell Peppers", "Green Beans"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)





#Treasure Map:

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

column = int( position[0] ) - 1
row = int( position[1] ) - 1

selected_row = map[row]
selected_row[column] = "⬛"



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

