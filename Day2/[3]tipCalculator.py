#A simple python program to calculate tip
print("Welcome to the tip calculator.")

total_amount = float(input("What was the total amount: $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
number_of_people = int(input("How many people to split the bill?"))

amount_after_tip = total_amount + total_amount * (tip_percentage / 100)
amount_for_each_person = round(amount_after_tip / number_of_people , 2)

print(f"Each person should pay {amount_for_each_person}")