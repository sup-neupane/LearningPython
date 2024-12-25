#Steps To Debug: 



# 1. Define the problem: Untangle by correctly defining problem
# def my_function():
#     for i in range(1,20):
#         if i== 20:
#             print("You Got It!")
# my_function()

#This function is supposed to loop from 1 to 20 and print "You Got It" when i is 20 
#But the range of i is only [1,20)
#Correct code:
# def my_function():
#     for i in range(1,21):
#         if i== 20:
#             print("You Got It!")
# my_function()




#2. Reproduce the bug
# from random import randint
# dice_imgs = ["⓵", "⓶", "⓷", "⓸", "⓹", "⓺"]
# dice_num = randint(1,6)
# print(dice_imgs[dice_num])

#This works alright at times but sometimes gives error
#So we need to reproduce the case where it gives an error by hardcoding which value from 1 to 6 causes error like:
# dice_num = 1
# dice_num = 2
# dice_num = 3 ... and so on
#So 6 causes an error
#Since the index of list starts from 0 so we need integers from 0-5 so:
# from random import randint
# dice_imgs = ["⓵", "⓶", "⓷", "⓸", "⓹", "⓺"]
# dice_num = randint(0,5)
# print(dice_imgs[dice_num])




#3. Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z")

#If you input 1994 it does nothing so act computer and evaluate each line for year = 1994
#So none of the condition is True for 1994 so the correct code is:
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year >= 1994:
#     print("You are a Gen Z")


#4. Fix the errors
# age = input("Enter your age: ")
# if age > 18:
# print("You can drive at age of {age}")

#The above line of code creates a read line below print so fix that by properly indenting before proceeding
#When you run after indenting, you should see type error in console. So properly typecast string to int
#Still it dosent print age so convert the statement to be printed  to f string
# age = int(input("Enter your age: "))
# if age > 18:
#     print(f"You can drive at age of {age}")



#5. Print of ten to squash those bugs
# pages = 0
# words_per_page = 0
# pages = int(input("Number of pages: "))
# words_per_page == int(input("Number of words per page: "))
# total_words = pages * words_per_page
# print(total_words)


#The output will be 0 if you print the pages and words_per_page after input you should see words_per_page is 0
#This is because we use comparison operator == instead of assignment operator
# pages = 0
# words_per_page = 0
# pages = int(input("Number of pages: "))
# words_per_page = int(input("Number of words per page: "))
# total_words = pages * words_per_page
# print(total_words)



#6. Use a debugger:
#You may use pythontutor.com to visulalize your code