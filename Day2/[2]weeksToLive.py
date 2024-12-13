# A program that prints weeks days weeks and months left in your life if you live up to 90
age = input("Enter your age")

years_to_live = 90 - int(age)

days_to_live =  years_to_live * 365
weeks_to_live =  years_to_live * 52
months_to_live = years_to_live * 12

print(f"You have {days_to_live} days to live, {weeks_to_live} weeks to live, {months_to_live} months to live")